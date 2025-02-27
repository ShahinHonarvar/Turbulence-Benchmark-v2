def palindrome_of_length_at_least_n(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word.lower() == word.lower()[::-1]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 19, len(s) + 1):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes