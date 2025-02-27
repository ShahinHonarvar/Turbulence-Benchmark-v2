def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word.lower() == word.lower()[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha()))
    english_letters = get_english_letters(s[1:8])
    if len(english_letters) < 5:
        return set()
    palindromes = set()
    for i in range(len(english_letters) - 4):
        for j in range(i + 1, len(english_letters) - 3):
            substring = english_letters[i:j]
            for k in range(j + 1, len(english_letters) + 1):
                if is_palindrome(substring + english_letters[j:k]):
                    palindromes.add(substring + english_letters[j:k])
    return palindromes