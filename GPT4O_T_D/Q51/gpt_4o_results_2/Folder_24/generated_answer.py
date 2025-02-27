from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        normalized = ''.join(sorted(s.lower()))
        if len(normalized) >= 3:
            anagram_dict[normalized].append(s)
    pair_count = 0
    for word_list in anagram_dict.values():
        if len(word_list) > 1:
            n = len(word_list)
            pair_count += n * (n - 1) // 2
            if pair_count > 96:
                return False
    return True