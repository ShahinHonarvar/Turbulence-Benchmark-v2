def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    palindromes = set()
    for i in range(5, min(9, len(s))):
        substring = s[i].lower()
        if substring.isalpha():
            palindromes.add(substring)
    for i in range(5, min(9, len(s))):
        for j in range(i + 1, min(9, len(s)) + 1):
            substring = s[i:j].lower()
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes