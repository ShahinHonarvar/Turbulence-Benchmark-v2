from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    count = 0
    for anagrams in anagram_map.values():
        if len(anagrams) >= 2:
            num_pairs = len(anagrams) * (len(anagrams) - 1) // 2
            count += num_pairs
            if count >= 3:
                return True
    return False