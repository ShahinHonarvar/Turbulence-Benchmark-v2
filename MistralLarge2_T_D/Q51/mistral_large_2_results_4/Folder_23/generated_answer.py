from collections import defaultdict

def if_contains_anagrams(lst):
    pairs = 0
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    for group in anagrams.values():
        if len(group) > 1:
            pairs += len(group) * (len(group) - 1) // 2
            if pairs > 49:
                return False
    return True