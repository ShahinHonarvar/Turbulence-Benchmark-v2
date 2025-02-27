def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    s_letters = get_english_letters(s[:8])
    palindromes = set()
    for i in range(1, len(s_letters)):
        for perm in set(s_letters[:i]):
            for j in range(i, len(s_letters) + 1):
                word = s_letters[i - j:i] + perm + s_letters[i:i + j]
                if is_palindrome(word) and len(word) >= 7:
                    palindromes.add(word)
    return palindromes