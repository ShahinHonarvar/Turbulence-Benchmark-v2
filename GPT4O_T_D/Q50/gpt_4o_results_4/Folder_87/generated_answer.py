from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagram_map = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagram_map[sorted_word].append(word)
    for anagram_list in anagram_map.values():
        pair_count = len(anagram_list) * (len(anagram_list) - 1) // 2
        count += pair_count
        if count >= 88:
            return True
    return False