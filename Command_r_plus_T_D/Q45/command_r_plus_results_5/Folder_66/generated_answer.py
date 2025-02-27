def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    english_letters = get_english_letters(s[:6])
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 1, len(english_letters) + 1):
            sub_str = english_letters[i:j]
            if len(sub_str) >= 5 and is_palindrome(sub_str):
                palindromes.add(sub_str)
    return palindromes