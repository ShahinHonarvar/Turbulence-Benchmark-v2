def palindrome_of_length_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    length = 78
    palindromes = set()
    for i in range(len(s) - length + 1):
        if is_palindrome(s[i:i + length]):
            palindromes.add(s[i:i + length])
    return palindromes