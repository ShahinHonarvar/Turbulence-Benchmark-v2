from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            anagrams[key].append(word)
    count = 0
    for key, values in anagrams.items():
        if len(values) >= 2:
            count += len(values) * (len(values) - 1) // 2
    return count >= 42