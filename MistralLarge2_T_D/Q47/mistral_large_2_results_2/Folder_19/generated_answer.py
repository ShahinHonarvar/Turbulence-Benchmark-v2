def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x == x[::-1]
    substring = s[10:56]
    palindromes = set()
    for length in range(3, 8):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate.lower())
    return palindromes