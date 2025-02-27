def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(3, 9):
        for j in range(i + 1, 9):
            substring = s[i:j].lower()
            if all((char in english_letters for char in substring)):
                if is_palindrome(substring) and len(substring) >= 5:
                    palindromes.add(substring)
    return palindromes