from collections import defaultdict

def if_contains_anagrams(strings):
    count = defaultdict(list)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        count[sorted_str].append(s)
    anagram_pairs = sum((1 for key in count if len(count[key]) >= 2 and len(key) >= 3))
    return anagram_pairs >= 22