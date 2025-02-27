def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[127:289]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(119, 142):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes