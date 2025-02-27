from collections import Counter

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string not in anagrams:
                anagrams[sorted_string] = [string]
            else:
                anagrams[sorted_string].append(string)
    pairs = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            pairs += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
        if pairs >= 26:
            return True
    return False