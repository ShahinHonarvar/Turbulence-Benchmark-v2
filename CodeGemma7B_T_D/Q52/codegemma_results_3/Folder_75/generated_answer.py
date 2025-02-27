def palindrome_of_length_n(text):

    def is_palindrome(word):
        word = word.lower()
        return word == word[::-1]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            palindrome = text[i:j]
            if is_palindrome(palindrome) and len(palindrome) == 80:
                palindromes.add(palindrome)
    return palindromes