from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_count[sorted_word] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs_count <= 96