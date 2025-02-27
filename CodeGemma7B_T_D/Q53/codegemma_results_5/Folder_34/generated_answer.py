from itertools import product

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for size in range(68, len(text) + 1):
        for start_index in range(len(text) - size + 1):
            substring = text[start_index:start_index + size]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes