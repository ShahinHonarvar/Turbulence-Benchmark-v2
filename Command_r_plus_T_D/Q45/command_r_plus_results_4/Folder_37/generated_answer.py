def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    s = get_english_letters(s)
    if len(s) < 5:
        return set()
    palindromes = set()
    for i in range(1, min(5, len(s))):
        for j in range(i + 1, min(i + 4, len(s)) + 1):
            substring = s[i:j]
            if is_palindrome(substring) and len(substring) >= 5:
                palindromes.add(substring)
    return palindromes