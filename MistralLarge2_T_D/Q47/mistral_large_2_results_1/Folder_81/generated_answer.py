def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    s = s[12:123]
    length = len(s)
    for length_of_palindrome in range(12, 221):
        for i in range(length - length_of_palindrome + 1):
            substring = s[i:i + length_of_palindrome].lower()
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes