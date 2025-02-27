def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    english_letters = get_english_letters(s[1:8])
    if len(english_letters) < 7:
        return set()
    palindromes = set()
    for i in range(len(english_letters) - 6):
        for j in range(i + 1, len(english_letters) - 5 + i):
            substring = english_letters[i:j] + english_letters[j:i:-1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes