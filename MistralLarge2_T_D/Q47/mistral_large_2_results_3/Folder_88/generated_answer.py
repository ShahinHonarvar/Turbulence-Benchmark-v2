def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[11:88].lower()
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes