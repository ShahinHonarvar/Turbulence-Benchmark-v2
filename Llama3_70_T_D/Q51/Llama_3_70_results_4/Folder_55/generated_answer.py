from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    pairs = set()
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) < 3:
            continue
        sorted_word = ''.join(sorted(word_lower))
        anagrams[sorted_word].append(word_lower)
    for k, v in anagrams.items():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                pairs.add(tuple(sorted([v[i], v[j]])))
    return len(pairs) <= 44