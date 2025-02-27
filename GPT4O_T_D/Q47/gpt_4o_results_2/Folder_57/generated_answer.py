def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s[16:95])).lower()
    palindrome_set = set()
    for length in range(39, 53):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindrome_set.add(substring)
    return palindrome_set