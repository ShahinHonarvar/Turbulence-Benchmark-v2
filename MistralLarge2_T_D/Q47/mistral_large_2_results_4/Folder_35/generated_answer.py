def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    allowed_lengths = range(14, 40)
    palindromes = set()
    substr = s[34:91].lower()
    for length in allowed_lengths:
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes