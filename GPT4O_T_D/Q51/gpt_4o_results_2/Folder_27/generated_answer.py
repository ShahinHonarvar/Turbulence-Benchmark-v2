from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    pair_count = 0
    for anagram_list in anagram_map.values():
        n = len(anagram_list)
        if n > 1:
            pair_count += n * (n - 1) // 2
            if pair_count > 113:
                return False
    return True