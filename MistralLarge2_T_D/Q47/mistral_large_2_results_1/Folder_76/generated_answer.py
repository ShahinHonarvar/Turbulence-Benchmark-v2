def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        return s == s[::-1]
    substring = string[101:293].lower()
    palindromes = set()
    for length in range(154, 183):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes