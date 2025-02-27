def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    substring = text[16:61]
    palindromes = set()
    for length in range(16, 40):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate.lower())
    return palindromes