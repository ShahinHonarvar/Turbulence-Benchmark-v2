def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    s = get_english_letters(s)
    if len(s) < 7:
        return set()
    palindromes = set()
    for i in range(3, 9):
        for j in range(i + 1, 9):
            substring = s[i:j]
            if len(substring) >= 7 and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes