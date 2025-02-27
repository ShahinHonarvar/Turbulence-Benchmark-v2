from collections import defaultdict

def if_contains_anagrams(str_list):
    str_map = defaultdict(set)
    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        str_map[sorted_word].add(word)
    anagram_count = 0
    for anagram_set in str_map.values():
        if len(anagram_set) > 1:
            anagram_count += len(anagram_set) - 1
            if anagram_count > 206:
                return False
    return True