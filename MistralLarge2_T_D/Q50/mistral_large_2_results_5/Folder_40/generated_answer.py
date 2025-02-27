from collections import defaultdict

def if_contains_anagrams(lst):

    def normalized_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        normalized = normalized_string(word)
        anagram_dict[normalized].append(word)
    anagram_count = sum((len(v) >= 2 for v in anagram_dict.values()))
    return anagram_count >= 3