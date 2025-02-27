def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    s = get_english_letters(s)
    palindromes = set()
    for i in range(len(s[:5]) + 1):
        for j in range(len(s[:5]) - i + 1):
            substring = s[j:j + i]
            if is_palindrome(substring) and len(substring) >= 4:
                palindromes.add(substring)
    return palindromes