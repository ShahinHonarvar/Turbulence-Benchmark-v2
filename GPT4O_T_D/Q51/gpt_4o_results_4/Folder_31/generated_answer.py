from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_groups = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_groups[sorted_word].append(word)
    anagram_pairs = 0
    for words in anagram_groups.values():
        if len(words) > 1:
            anagram_pairs += len(words) * (len(words) - 1) // 2
        if anagram_pairs > 65:
            return False
    return True