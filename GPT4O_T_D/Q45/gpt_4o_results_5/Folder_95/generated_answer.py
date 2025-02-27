def palindromes_between_indices(s):

    def can_form_palindrome(counts):
        odd_count = sum((count % 2 for count in counts.values()))
        return odd_count <= 1
    substring = s[7:9].lower()
    letter_counts = {}
    for char in substring:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    if not can_form_palindrome(letter_counts):
        return set()

    def generate_half_palindrome(current, counts):
        if sum(counts.values()) == 0:
            palindromes.add(current + current[::-1])
            return
        for char in counts:
            if counts[char] > 0:
                new_counts = counts.copy()
                new_counts[char] -= 1
                half_palindrome = current + char
                generate_half_palindrome(half_palindrome, new_counts)
    if not letter_counts:
        return set()
    palindromes = set()
    for char in letter_counts:
        if letter_counts[char] % 2 == 1:
            counts = letter_counts.copy()
            counts[char] -= 1
            generate_half_palindrome(char, counts)
    return {p for p in palindromes if len(p) >= 3}