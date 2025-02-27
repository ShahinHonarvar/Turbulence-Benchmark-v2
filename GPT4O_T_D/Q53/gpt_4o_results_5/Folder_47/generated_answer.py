def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    normalized_s = ''.join(filter(str.isalpha, s)).lower()
    n = 77
    palindromes = set()
    for start in range(len(normalized_s)):
        for end in range(start + n, len(normalized_s) + 1):
            substring = normalized_s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes