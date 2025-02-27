from collections import defaultdict

def if_contains_anagrams(str_list):
    str_map = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        str_map[sorted_word].append(word)
    anagram_count = 0
    for anagram_list in str_map.values():
        if len(anagram_list) >= 3:
            anagram_count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return anagram_count <= 52