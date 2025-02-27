from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        key = ''.join(sorted(word.lower()))
        anagrams[key].append(word)
    count = sum((1 for group in anagrams.values() if len(group) >= 2))
    return count >= 74