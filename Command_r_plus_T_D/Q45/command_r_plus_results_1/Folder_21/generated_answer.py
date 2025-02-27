def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    s = s[1:9]
    english_letters = get_english_letters(s)
    all_palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 7, len(english_letters) + 1):
            substring = english_letters[i:j]
            if is_palindrome(substring):
                all_palindromes.add(substring)
    return all_palindromes