def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    s = get_english_letters(s)
    palindromes = set()
    for i in range(1, min(len(s), 8)):
        for j in range(i + 2, min(len(s), i + 8)):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes