from collections import defaultdict

def if_contains_anagrams(text):
    anagrams = defaultdict(list)
    for word in text:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3:
            anagrams[key].append(word)
    for group in anagrams.values():
        if len(group) >= 47:
            return True
    return False