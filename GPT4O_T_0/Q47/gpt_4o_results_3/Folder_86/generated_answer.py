def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[30:96]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(34, 56):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes