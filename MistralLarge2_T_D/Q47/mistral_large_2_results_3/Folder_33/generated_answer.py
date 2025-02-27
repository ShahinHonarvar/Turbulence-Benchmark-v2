def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[130:296]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(103, 159):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes