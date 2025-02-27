from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_groups[sorted_word] += 1
    pair_count = sum([count * (count - 1) // 2 for count in anagram_groups.values()])
    return pair_count >= 140