from collections import defaultdict

def palindrome_of_length_at_least_n(text):

    def is_palindrome(word):
        return word == word[::-1] and all((char.isalpha() for char in word))
    char_counts = defaultdict(int)
    for char in text.lower():
        char_counts[char] += 1
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 57, len(text) + 1):
            palindrome = text[i:j]
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes