def palindromes_between_indices(s: str) -> set:

    def is_palindrome(s):
        return s == s[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    s = s[2:8]
    english_letters = get_english_letters(s)
    unique_letters = set(english_letters)
    if len(unique_letters) < 3:
        return set()
    palindromes = set()
    for p in english_letters:
        if is_palindrome(p) and len(p) >= 6:
            palindromes.add(p)
    return palindromes