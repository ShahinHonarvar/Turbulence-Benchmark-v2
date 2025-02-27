def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    middle_part = s[5:8].lower()
    english_letters = ''.join((c for c in middle_part if c.isalpha()))
    palindromes = set()

    def can_form_palindrome(letters):
        count = {}
        for letter in letters:
            count[letter] = count.get(letter, 0) + 1
        odd_count = sum((1 for cnt in count.values() if cnt % 2 != 0))
        return odd_count <= 1

    def generate_palindrome(letters, half):
        reverse_half = half[::-1]
        palindromes.add(half + reverse_half)
        for i in range(len(half)):
            for j in range(i + 1, len(half)):
                new_half = half[:i] + half[j:j + 1] + half[i + 1:j] + half[i:i + 1] + half[j + 1:]
                new_palindrome = new_half + reverse_half
                if new_palindrome not in palindromes:
                    palindromes.add(new_palindrome)
    if can_form_palindrome(english_letters):
        unique_half = ''.join(sorted(set(english_letters)))
        if len(unique_half) >= 2:
            generate_palindrome(english_letters, unique_half)
    return {p for p in palindromes if len(p) >= 4}