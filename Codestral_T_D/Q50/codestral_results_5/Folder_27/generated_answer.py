from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            d[''.join(sorted(word.lower()))].append(word)
    return sum((len(words) * (len(words) - 1) // 2 for words in d.values())) >= 86