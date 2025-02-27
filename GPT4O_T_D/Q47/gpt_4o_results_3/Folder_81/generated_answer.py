def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s[12:123])).lower()
    found_palindromes = set()
    n = len(s)
    for length in range(12, 221):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                found_palindromes.add(s[i:i + length])
    return found_palindromes