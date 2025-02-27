def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    s_letters = get_english_letters(s)
    s_letters = s_letters[:4]
    palindromes = set()
    for i in range(len(s_letters)):
        for j in range(i + 1, len(s_letters) + 1):
            substring = s_letters[i:j]
            if is_palindrome(substring) and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes