from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted((c.lower() for c in s if c.isalpha())))
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_dict[normalize(s)].append(s)
    anagram_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_dict.values()))
    return anagram_pairs <= 20