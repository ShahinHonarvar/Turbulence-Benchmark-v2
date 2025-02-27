def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[44:100]
    palindromes = set()
    for length in range(13, 43):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes