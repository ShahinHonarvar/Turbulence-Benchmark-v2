def palindromes_of_specific_lengths(s):

    def is_palindrome(string):
        return string == string[::-1]
    palindromes = set()
    substring = s[11:88].lower()
    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes