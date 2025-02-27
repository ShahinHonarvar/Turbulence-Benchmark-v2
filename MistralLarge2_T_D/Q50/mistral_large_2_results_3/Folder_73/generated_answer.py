from collections import defaultdict

def if_contains_anagrams(lst):
    count = defaultdict(int)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        count[sorted_word] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return anagram_pairs >= 91