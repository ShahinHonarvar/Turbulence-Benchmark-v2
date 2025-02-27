from collections import Set

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

def find_palindromes(input_string):
    palindromes = set()
    for i in range(len(input_string) - 9):
        for j in range(i, len(input_string) - i):
            word = input_string[i:j + 1]
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes

def palindrome_of_length_at_least_n(input_string, n):
    if n < 10:
        raise ValueError("Input 'n' must be at least 10")
    palindromes = find_palindromes(input_string)
    return {word for word in palindromes if len(word) >= n}