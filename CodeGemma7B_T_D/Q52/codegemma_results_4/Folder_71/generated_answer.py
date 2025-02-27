from itertools import product

def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes