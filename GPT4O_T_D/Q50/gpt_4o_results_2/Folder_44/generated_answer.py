from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    count = 0
    for anagram_list in anagram_map.values():
        num_anagrams = len(anagram_list)
        if num_anagrams > 1:
            count += num_anagrams * (num_anagrams - 1) // 2
            if count >= 44:
                return True
    return False