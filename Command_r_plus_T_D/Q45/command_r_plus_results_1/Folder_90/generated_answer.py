def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join(filter(str.isalpha, s)).lower()
    english_letters = get_english_letters(s[:6])
    if len(english_letters) < 4:
        return set()
    palindromes = set()
    for i in range(len(english_letters) - 3):
        for j in range(i + 4, len(english_letters) + 1):
            palindrome = english_letters[i:j]
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes