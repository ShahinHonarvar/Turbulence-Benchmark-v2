from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_map = defaultdict(int)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_count += anagram_map[sorted_word]
        anagram_map[sorted_word] += 1
    return anagram_count >= 72