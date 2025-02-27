def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    s = s[:9]
    english_letters = get_english_letters(s)
    all_palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 7, len(english_letters) + 1):
            substring = english_letters[i:j]
            for word in substring.split():
                if is_palindrome(word) and len(word) >= 7:
                    all_palindromes.add(word)
    return all_palindromes