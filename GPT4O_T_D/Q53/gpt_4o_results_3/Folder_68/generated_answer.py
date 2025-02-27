def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for start in range(len(s)):
        for end in range(start + 21, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes