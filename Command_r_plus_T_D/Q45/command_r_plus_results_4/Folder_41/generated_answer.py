def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    palindromes = set()
    for i in range(2, len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring.lower()) and (len(substring) >= 3):
                palindromes.add(substring)
    return palindromes