def palindromes_of_specific_lengths(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word.lower() == word.lower()[::-1]
    palindromes = set()
    substring = s[15:61]
    for length in range(16, 40):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length].isalpha() and is_palindrome(substring[i:i + length]):
                palindromes.add(substring[i:i + length])
    return palindromes