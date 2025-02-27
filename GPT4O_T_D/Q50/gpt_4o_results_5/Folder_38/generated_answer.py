from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    lookup = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            lookup[sorted_chars(word)] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in lookup.values()))
    return anagram_pairs >= 24