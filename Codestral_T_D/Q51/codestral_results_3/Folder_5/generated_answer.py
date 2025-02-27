from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            anagrams[key].append(string)
    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count <= 4