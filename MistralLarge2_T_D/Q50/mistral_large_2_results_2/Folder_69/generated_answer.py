from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        key = ''.join(sorted(word.lower()))
        anagrams[key].append(word)
    anagram_count = sum((1 for group in anagrams.values() if len(group) > 1))
    return anagram_count >= 188