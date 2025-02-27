from re import *

def palindrome_of_length_n(text):
    return set(filter(lambda x: palindrome_checker(text.lower(), x), [text[a:b + 1] for a in range(len(text)) for b in range(a, len(text))]))

def palindrome_checker(text, word):
    return text == text[::-1] and len(word) == 76 and word.isalpha()