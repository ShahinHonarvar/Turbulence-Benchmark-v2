def palindrome_of_length_at_least_n(txt):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(len(txt)):
        for j in range(i + 3, len(txt) + 1):
            word = txt[i:j].lower()
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes