from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    for word_list in anagram_map.values():
        n = len(word_list)
        if n > 1:
            anagram_count += n * (n - 1) // 2
        if anagram_count >= 66:
            return True
    return False