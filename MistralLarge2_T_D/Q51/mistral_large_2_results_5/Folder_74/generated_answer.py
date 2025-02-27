from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    pairs_count = 0
    for group in anagram_dict.values():
        pairs_count += len(group) * (len(group) - 1) // 2
    return pairs_count <= 57