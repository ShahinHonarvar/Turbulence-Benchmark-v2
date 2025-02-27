def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 137, len(s) + 1):
            word = s[i:j]
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes