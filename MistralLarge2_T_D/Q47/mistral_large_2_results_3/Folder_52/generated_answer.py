def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[44:100]
    palindromes = set()
    for length in range(13, 43):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length].lower()
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes