def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    substring = s[125:284]
    length_range = range(109, 127)
    palindromes = set()
    for length in length_range:
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate.lower())
    return palindromes