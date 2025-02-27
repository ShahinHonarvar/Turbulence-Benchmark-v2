from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_map = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted([char for char in word if char.isalpha()], key=str.lower))
        if len(sorted_word) < 3:
            continue
        anagram_map[sorted_word].append(word)
    num_pairs = 0
    for anagram_list in anagram_map.values():
        num_pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return num_pairs <= 66