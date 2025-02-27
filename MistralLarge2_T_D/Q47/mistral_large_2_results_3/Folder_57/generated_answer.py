def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    substr = s[16:95].lower()
    for length in range(39, 53):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes