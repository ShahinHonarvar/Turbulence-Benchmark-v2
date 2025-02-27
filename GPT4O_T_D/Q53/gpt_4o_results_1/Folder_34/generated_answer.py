def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    substr_length = 68
    for start_idx in range(len(s)):
        for length in range(substr_length, len(s) - start_idx + 1):
            substring = s[start_idx:start_idx + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes