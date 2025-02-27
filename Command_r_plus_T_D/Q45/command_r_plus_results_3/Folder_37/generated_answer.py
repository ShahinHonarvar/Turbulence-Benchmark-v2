def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join(filter(str.isalpha, s)).lower()
    english_letters = get_english_letters(s[1:5])
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 1, len(english_letters) + 1):
            substring = english_letters[i:j]
            if is_palindrome(substring) and len(substring) >= 5:
                palindromes.add(substring)
    return palindromes