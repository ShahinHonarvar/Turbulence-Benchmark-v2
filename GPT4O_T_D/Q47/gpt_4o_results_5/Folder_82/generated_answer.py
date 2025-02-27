def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        clean_sub = ''.join((c.lower() for c in sub if c.isalpha()))
        return clean_sub == clean_sub[::-1]
    palindromes = set()
    substr = s[3:301]
    for length in range(30, 301):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes