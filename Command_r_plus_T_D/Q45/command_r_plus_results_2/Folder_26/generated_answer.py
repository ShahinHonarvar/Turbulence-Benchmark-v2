def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(substring: str) -> str:
        return ''.join((char for char in substring if char.isalpha()))
    palindromes = set()
    substring = s[4:7]
    english_letters = get_english_letters(substring)
    for i in range(len(english_letters)):
        for j in range(i + 3, len(english_letters) + 1):
            window = english_letters[i:j]
            if is_palindrome(window):
                palindromes.add(window)
    return palindromes