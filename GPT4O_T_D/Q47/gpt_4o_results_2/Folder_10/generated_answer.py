def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        sub = ''.join(filter(str.isalpha, sub)).lower()
        return sub == sub[::-1]
    palindromes = set()
    for start in range(16, min(61, len(s))):
        for end in range(start + 16, min(start + 40, len(s) + 1)):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes