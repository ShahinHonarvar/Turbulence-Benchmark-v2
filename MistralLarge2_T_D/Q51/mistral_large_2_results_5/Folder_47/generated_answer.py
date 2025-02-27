from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_count[sorted_word] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pair_count <= 366