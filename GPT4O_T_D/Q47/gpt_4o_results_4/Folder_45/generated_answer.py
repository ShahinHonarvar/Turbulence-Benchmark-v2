def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr[::-1].lower()
    n = len(s)
    result = set()
    s = ''.join(filter(str.isalpha, s))
    for start in range(max(0, 70), min(n, 141)):
        for end in range(start + 3, min(start + 61, n + 1)):
            substring = s[start:end]
            if is_palindrome(substring):
                result.add(substring.lower())
    return result