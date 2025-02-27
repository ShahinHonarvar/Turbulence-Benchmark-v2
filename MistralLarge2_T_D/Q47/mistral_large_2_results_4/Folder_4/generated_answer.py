def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    substring = string[12:93]
    palindromes = set()
    for length in range(17, 67):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub.lower())
    return palindromes