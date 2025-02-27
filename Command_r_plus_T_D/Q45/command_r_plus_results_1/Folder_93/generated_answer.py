def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word.lower() == word.lower()[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(2, 8):
        for j in range(i + 1, 8):
            substring = s[i:j]
            if all((char in english_letters for char in substring.lower())):
                if is_palindrome(substring):
                    palindromes.add(substring)
    return {p for p in palindromes if len(p) >= 6}