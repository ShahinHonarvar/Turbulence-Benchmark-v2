def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    english_letters = get_english_letters(s[3:5])
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 3 - 1, len(english_letters)):
            substring = english_letters[i:j + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes