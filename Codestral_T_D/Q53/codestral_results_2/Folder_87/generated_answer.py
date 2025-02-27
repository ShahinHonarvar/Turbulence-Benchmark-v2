def palindrome_of_length_at_least_n(text):
    palindromes = set()

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    for i in range(len(text)):
        for j in range(i + 18, len(text) + 1):
            substring = text[i:j]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring)
    return palindromes