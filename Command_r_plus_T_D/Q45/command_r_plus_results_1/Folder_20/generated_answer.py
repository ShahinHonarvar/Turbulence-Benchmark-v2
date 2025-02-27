def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    s_letters = get_english_letters(s[2:9])
    palindromes = set()
    for i in range(4, len(s_letters) + 1):
        for j in range(len(s_letters) - i + 1):
            substring = s_letters[j:j + i]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes