def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    s = s[:8]
    english_letters = get_english_letters(s)
    all_palindromes = set()
    for i in range(1, len(english_letters)):
        for j in range(len(english_letters) - i + 1):
            substring = english_letters[j:j + i]
            if is_palindrome(substring) and len(substring) >= 4:
                all_palindromes.add(substring)
    return all_palindromes