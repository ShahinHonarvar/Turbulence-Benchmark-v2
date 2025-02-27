from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        count = Counter(word)
        key = ''.join(count.most_common())
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    for values in anagrams.values():
        pairs = len(values) * (len(values) - 1) // 2
        if pairs > 52:
            return False
    return True