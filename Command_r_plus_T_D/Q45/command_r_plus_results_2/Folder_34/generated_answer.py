def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    s_english_letters = get_english_letters(s)
    palindromes = set()
    for i in range(5, min(len(s_english_letters), 8)):
        for j in range(i + 1, min(len(s_english_letters), 9)):
            substring = s_english_letters[i:j]
            if is_palindrome(substring) and len(substring) >= 4:
                palindromes.add(substring)
    return palindromes