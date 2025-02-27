from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for s in strings:
        clean_s = ''.join(sorted((c.lower() for c in s if c.isalpha())))
        if len(clean_s) >= 3:
            anagram_dict[clean_s] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return pairs_count <= 464