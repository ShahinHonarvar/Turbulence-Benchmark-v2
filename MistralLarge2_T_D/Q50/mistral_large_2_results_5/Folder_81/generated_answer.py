from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_pairs_count = 0
    for key in anagram_dict:
        words = anagram_dict[key]
        if len(words) > 1:
            anagram_pairs_count += len(words) * (len(words) - 1) // 2
    return anagram_pairs_count >= 16