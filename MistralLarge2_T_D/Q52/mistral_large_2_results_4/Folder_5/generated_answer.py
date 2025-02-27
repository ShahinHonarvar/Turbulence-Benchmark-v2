def palindrome_of_length_n(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    length = 17
    palindromes = set()
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if is_palindrome(substr) and substr.isalpha():
            palindromes.add(substr)
    return palindromes