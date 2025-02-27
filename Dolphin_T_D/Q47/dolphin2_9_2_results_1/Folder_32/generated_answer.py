def palindromes_of_specific_lengths(s):
    substr = s[15:77]
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1] and s.isalpha() == 1
    for i in range(43, 48):
        for j in range(len(substr) - i + 1):
            s = substr[j:j + i]
            if is_palindrome(s.lower()):
                palindromes.add(s)
    return palindromes