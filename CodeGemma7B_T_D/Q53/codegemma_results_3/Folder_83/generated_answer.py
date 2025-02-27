def palindrome_of_length_at_least_n(text):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 60, len(text) + 1):
            word = text[i:j]
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes