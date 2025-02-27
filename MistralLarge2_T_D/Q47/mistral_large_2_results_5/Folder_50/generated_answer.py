def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substr = s[36:93].lower()
    palindromes = set()
    for length in range(10, 36):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes