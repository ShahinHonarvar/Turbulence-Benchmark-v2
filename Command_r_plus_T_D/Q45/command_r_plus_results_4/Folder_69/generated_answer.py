def palindromes_between_indices(s: str) -> set:

    def is_palindrome(s):
        return s == s[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    s_letters = get_english_letters(s)
    if len(s_letters) < 4:
        return set()
    palindromes = set()
    for i in range(len(s_letters) - 3):
        for j in range(i + 1, len(s_letters) - 2):
            substring = s_letters[i:j + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes