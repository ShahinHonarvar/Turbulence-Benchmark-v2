from itertools import product

def palindrome_of_length_n(text):
    text = text.lower()
    char_list = set(text)
    sample = list('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for p in product(sample, repeat=93):
        string = ''.join(p)
        if len(string) == 186 and string in text:
            result.add(string)
    return result