from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_count[sorted_word] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pair_count >= 38