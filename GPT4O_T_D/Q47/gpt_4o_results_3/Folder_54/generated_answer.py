def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[27:78]
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    palindromes = set()
    for length in range(18, 20):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes