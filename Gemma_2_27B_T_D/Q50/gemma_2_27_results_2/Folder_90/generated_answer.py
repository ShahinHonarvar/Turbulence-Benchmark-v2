from collections import defaultdict

def if_contains_anagrams(words):
    anagram_counts = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_counts[sorted_word] += 1
    pair_count = 0
    for count in anagram_counts.values():
        pair_count += count * (count - 1) // 2
    return pair_count >= 177