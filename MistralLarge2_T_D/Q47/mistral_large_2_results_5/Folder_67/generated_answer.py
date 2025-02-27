def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x == x[::-1]
    substring = s[65:100].lower()
    palindromes = set()
    for length in range(26, 34):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes