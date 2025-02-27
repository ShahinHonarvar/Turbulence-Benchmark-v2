def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    s = get_english_letters(s)
    possible_palindromes = set()
    for i in range(len(s) - 6):
        for j in range(i + 7, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                possible_palindromes.add(substring)
    return {p for p in possible_palindromes if len(p) >= 7}