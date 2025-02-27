def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    s = s[30:85].lower()
    for length in range(12, 21):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes