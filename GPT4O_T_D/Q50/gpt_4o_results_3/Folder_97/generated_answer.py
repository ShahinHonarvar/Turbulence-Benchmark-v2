from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_map = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word] += 1
    count = sum((n * (n - 1) // 2 for n in anagram_map.values() if n > 1))
    return count >= 123