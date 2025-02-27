from functools import partial

def palindrome_of_length_at_least_n(text):
    set_of_palindrome = set()
    text = ''.join((ch for ch in text if ch.isalpha()))
    text = text.lower()
    for i in range(0, len(text) - 32):
        for j in range(i + 32, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                set_of_palindrome.add(substring)
    return set_of_palindrome