def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    substring = s[11:84].lower()
    palindromes = set()
    for length in range(13, 67):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes