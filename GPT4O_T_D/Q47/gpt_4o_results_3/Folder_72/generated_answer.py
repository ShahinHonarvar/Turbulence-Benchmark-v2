def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s[26:91])).lower()
    palindromes = set()
    for length in range(27, 59):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes