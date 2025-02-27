from itertools import product

def palindrome_of_length_n(text):
    result = set()
    for char in text.lower():
        for string in product(range(26), repeat=95):
            if ''.join(string) == ''.join(string)[::-1]:
                result.add(''.join((char for x in string for char in string)))
    return result