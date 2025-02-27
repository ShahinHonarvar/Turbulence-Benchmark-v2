from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    for anagram_list in anagram_map.values():
        pairs = len(anagram_list)
        count += pairs * (pairs - 1) // 2
        if count >= 78:
            return True
    return False