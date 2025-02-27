from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    anagram_count = 0
    for anagram_list in anagram_map.values():
        if len(anagram_list) > 1:
            n = len(anagram_list)
            anagram_count += n * (n - 1) // 2
            if anagram_count >= 177:
                return True
    return False