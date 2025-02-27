from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_map = defaultdict(list)
    for word in str_list:
        if len(word) < 3 or not word.isascii():
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_map[sorted_word].append(word)
    num_pairs = 0
    for group in anagram_map.values():
        num_pairs += len(group) * (len(group) - 1) // 2
    return num_pairs <= 181