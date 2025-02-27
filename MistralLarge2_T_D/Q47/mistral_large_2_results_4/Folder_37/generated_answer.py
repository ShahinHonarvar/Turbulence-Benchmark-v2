def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x == x[::-1]
    substring = s[:10]
    palindromes = set()
    for length in range(3, 6):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment.isalpha() and is_palindrome(segment.lower()):
                palindromes.add(segment.lower())
    return palindromes