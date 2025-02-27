def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    substring = string[15:96].lower()
    for length in range(20, 67):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes