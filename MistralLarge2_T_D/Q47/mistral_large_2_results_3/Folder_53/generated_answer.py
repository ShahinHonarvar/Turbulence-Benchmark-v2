def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    for length in range(3, 11):
        for i in range(1, 299 - length + 2):
            sub = s[i:i + length]
            if sub.isalpha() and is_palindrome(sub.lower()):
                palindromes.add(sub.lower())
    return palindromes