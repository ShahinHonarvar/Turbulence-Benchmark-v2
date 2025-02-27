def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    s = get_english_letters(s)
    return set((w for w in s[0:4] if is_palindrome(w) and len(w) >= 3))