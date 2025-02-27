from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagram_map = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word] += 1
    for count_word in anagram_map.values():
        if count_word > 1:
            count += count_word * (count_word - 1) // 2
        if count >= 115:
            return True
    return False