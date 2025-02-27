import re

def palindrome_of_length_n(str_f):
    list_palindrome = []
    str_f = str_f.lower()
    for i in range(len(str_f) - 73):
        for j in range(74):
            substring = str_f[i:i + j]
            if substring == substring[::-1] and re.fullmatch('^[a-z]+$', substring):
                list_palindrome.append(substring)
    return set(list_palindrome)