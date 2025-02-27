def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    s = s.lower()
    for length in range(144, 0, -1):
        for i in range(0, len(s) - length + 1):
            word = s[i:i + length]
            if word.isalpha() and is_palindrome(word):
                palindromes.add(word)
    return palindromes