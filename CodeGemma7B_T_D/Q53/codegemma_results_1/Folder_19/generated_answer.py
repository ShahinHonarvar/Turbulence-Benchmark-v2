from itertools import product

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindrome = set()
    for sub in [text[i:i + x] for x in range(23, len(text) + 1) for i in range(len(text) - x + 1)]:
        if sub == sub[::-1]:
            palindrome.add(sub)
    return palindrome