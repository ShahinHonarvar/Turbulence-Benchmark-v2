def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    s_trimmed = s[:6]
    english_letters = get_english_letters(s_trimmed)
    all_palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 4, len(english_letters) + 1):
            substring = english_letters[i:j]
            if is_palindrome(substring):
                all_palindromes.add(substring)
    return all_palindromes