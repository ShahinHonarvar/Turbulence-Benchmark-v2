from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    pairs = {}
    for word in strings:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3 and key not in pairs:
            pairs[key] = Counter(word.lower())
            count += 1
    return count <= 92