def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    palindromes = set()
    for i in range(4, 8):
        for j in range(i + 1, 8):
            substring = s[i:j]
            if all((char.isalpha() for char in substring)):
                word = substring.lower()
                if is_palindrome(word) and len(word) >= 5:
                    palindromes.add(word)
    return palindromes