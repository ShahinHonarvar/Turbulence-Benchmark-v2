def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    for length in range(5, 81):
        for i in range(21):
            sub = s[i:i + length].lower()
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes