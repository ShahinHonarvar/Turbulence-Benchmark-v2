from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        key = ''.join(sorted([ch for ch in word.lower() if ch.isalpha()]))
        anagrams[key].append(word)
    return len(anagrams) <= 29