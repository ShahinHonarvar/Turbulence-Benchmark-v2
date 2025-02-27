def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[26:85]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(30, 47):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes