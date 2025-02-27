def palindrome_of_length_at_least_n(text):
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 144, len(text) + 1):
            word = text[i:j]
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes