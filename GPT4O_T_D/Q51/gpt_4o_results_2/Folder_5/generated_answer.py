from collections import defaultdict

def if_contains_anagrams(lst):
    pairs_count = 0
    anagram_dict = defaultdict(int)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        pairs_count += anagram_dict[sorted_word]
        anagram_dict[sorted_word] += 1
    return pairs_count <= 4