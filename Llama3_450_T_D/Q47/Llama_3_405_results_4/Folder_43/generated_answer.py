def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[41:90].lower()
    palindromes = set()
    for length in range(23, 39):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes