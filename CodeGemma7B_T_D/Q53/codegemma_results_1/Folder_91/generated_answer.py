def palindrome_of_length_at_least_n(text):
    text = text.lower()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 6, len(text) + 1):
            substring = text[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindrome