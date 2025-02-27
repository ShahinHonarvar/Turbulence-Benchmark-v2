from collections import Counter
        from itertools import permutations

def palindromes_between_indices(s):

    def can_form_palindrome(letters):
        letter_counts = Counter(letters)
        odd_count = sum((1 for count in letter_counts.values() if count % 2 != 0))
        return odd_count <= 1
    s_sub = s[4:7].lower()
    letters = ''.join(filter(str.isalpha, s_sub))
    palindromes = set()

    def generate_palindromes(half):
        if len(half) < 2:
            if can_form_palindrome(letters):
                if len(letters) >= 3:
                    palindromes.add(letters)
            return
        half_permutations = {''.join(p) for p in permutations(half)}
        for half_str in half_permutations:
            almost_palindrome = half_str + half_str[::-1]
            if can_form_palindrome(almost_palindrome):
                if len(almost_palindrome) >= 3:
                    palindromes.add(almost_palindrome)
            for middle_letter in letters:
                full_palindrome = half_str + middle_letter + half_str[::-1]
                if can_form_palindrome(full_palindrome):
                    if len(full_palindrome) >= 3:
                        palindromes.add(full_palindrome)
    generate_palindromes(letters[:len(letters) // 2])
    return palindromes