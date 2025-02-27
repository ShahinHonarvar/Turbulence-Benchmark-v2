import re

def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        string = string.lower()
        chars = re.findall('\\\\w', string)
        chars.sort()
        key = ''.join(chars)
        if key not in anagrams:
            anagrams[key] = [string]
        else:
            anagrams[key].append(string)
            count += 1
    return count >= 10