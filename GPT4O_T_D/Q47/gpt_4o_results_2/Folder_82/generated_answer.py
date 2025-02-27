def palindromes_of_specific_lengths(s: str) -> set:

    def is_palindrome(substr: str) -> bool:
        return substr.lower() == substr.lower()[::-1]
    s = ''.join(filter(str.isalpha, s[3:301]))
    result = set()
    n = len(s)
    for length in range(30, min(301, n + 1)):
        for start in range(n - length + 1):
            substr = s[start:start + length]
            if is_palindrome(substr):
                result.add(substr.lower())
    return result