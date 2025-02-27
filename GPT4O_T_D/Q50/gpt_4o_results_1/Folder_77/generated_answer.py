from collections import defaultdict

def if_contains_anagrams(word_list):
    anagram_map = defaultdict(int)
    for word in word_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word] += 1
    count = sum((count * (count - 1) // 2 for count in anagram_map.values()))
    return count >= 209