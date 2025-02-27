def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        return s == s[::-1]
    substring = string[18:66]
    palindromes = set()
    for length in range(23, 37):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and is_palindrome(sub.lower()):
                palindromes.add(sub)
    return palindromes