import re

def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(24, 68):
        if len(s) < 68:
            break
        if s[i] > 'f' and s[i] <= '|':
            if s[i] in vowels:
                result.append(s[i])
    return result if result else []