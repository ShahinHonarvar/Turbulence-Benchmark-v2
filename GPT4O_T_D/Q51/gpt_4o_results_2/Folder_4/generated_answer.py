from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            norm = normalize(word)
            anagrams[norm].append(word)
    pairs_count = 0
    for group in anagrams.values():
        if len(group) > 1:
            n = len(group)
            pairs_count += n * (n - 1) // 2
    return pairs_count <= 84