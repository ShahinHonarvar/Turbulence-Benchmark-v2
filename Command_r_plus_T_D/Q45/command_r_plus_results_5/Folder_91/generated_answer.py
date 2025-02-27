def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join(filter(str.isalpha, s)).lower()
    english_letters = get_english_letters(s[2:7])
    palindromes = set()
    for i in range(3, len(english_letters) + 1):
        for j in range(len(english_letters) - i + 1):
            substring = english_letters[j:j + i]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes