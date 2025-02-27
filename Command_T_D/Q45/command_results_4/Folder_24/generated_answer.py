import re

def palindromes_between_indices(s):
    s = re.sub('[a-z]', '', s)
    if len(s) < 4:
        return set()
    for i in range(len(s) - 1, len(s) - 3, -1):
        if s[i] == '[':
            s = s[:i] + s[i + 1:] + s[i:-1] + s[-1:]
            break
    return set(re.findall('((?<=.)[a-z]){4}(?=.)', s))