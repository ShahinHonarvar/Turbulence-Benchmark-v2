from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for word in string_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for anagram_group in anagram_dict.values():
        group_size = len(anagram_group)
        if group_size > 1:
            anagram_pairs += group_size * (group_size - 1) // 2
    return anagram_pairs >= 28