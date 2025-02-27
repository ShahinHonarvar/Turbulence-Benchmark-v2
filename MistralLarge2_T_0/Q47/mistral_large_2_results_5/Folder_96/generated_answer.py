def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[100:301]
    palindromes = set()
    for length in range(50, 101):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate.lower())
    return palindromes