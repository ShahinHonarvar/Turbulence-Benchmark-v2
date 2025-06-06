def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    substring = s[18:66].lower()
    for length in range(23, 37):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes