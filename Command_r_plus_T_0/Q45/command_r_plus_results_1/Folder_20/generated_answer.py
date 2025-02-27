def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    s = s[2:9]
    english_letters = get_english_letters(s)
    palindromes = set()
    for i in range(4, len(english_letters) + 1):
        for j in range(len(english_letters) - i + 1):
            substring = english_letters[j:j + i]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes