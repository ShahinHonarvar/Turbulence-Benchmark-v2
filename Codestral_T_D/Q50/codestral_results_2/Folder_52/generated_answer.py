from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    anagrams = {}
    for string in strings:
        string = string.lower()
        if len(string) >= 3:
            key = ''.join(sorted(string))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(string)
            count += len(anagrams[key]) - 1
    return count >= 58