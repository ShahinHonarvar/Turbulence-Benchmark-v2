def palindrome_of_length_at_least_n(s: str) -> set:

    def is_palindrome(candidate: str) -> bool:
        return candidate.lower() == candidate.lower()[::-1]
    palindromes = set()
    for i in range(len(s) - 80):
        for j in range(i + 81, len(s) + 1):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes