from collections import Counter

def if_contains_anagrams(words):
    anagram_groups = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word] += 1
            else:
                anagram_groups[sorted_word] = 1
    anagram_pairs = 0
    for count in anagram_groups.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
        if anagram_pairs > 257:
            return False
    return True