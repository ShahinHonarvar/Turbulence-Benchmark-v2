def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[41:90].lower()
    n = len(substring)
    palindromes = set()
    for length in range(23, 39):
        for i in range(n - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes