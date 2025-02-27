from collections import Counter

def if_contains_anagrams(lst):
    anagram_groups = {}
    for word in lst:
        lower_word = word.lower()
        if len(lower_word) < 3:
            continue
        sorted_word = ''.join(sorted(lower_word))
        anagram_groups[sorted_word] = anagram_groups.get(sorted_word, 0) + 1
    anagram_pairs_count = sum((count * (count - 1) // 2 for count in anagram_groups.values()))
    return anagram_pairs_count <= 19