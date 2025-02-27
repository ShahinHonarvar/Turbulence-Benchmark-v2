from collections import Counter

def if_contains_anagrams(lst):
    anagrams = Counter()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word] += 1
    pairs = 0
    for count in anagrams.values():
        if count > 1:
            pairs += count * (count - 1) // 2
    return pairs >= 246