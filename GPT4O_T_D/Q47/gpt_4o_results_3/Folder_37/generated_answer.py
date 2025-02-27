def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    palindromes = set()
    for length in range(3, 6):
        for i in range(10 - length + 1):
            substr = ''.join(filter(str.isalpha, s[i:i + length]))
            if len(substr) == length and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes