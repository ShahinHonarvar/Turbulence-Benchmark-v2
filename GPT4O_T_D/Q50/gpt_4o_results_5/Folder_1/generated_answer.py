from collections import defaultdict

def if_contains_anagrams(lst):
    word_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_dict[sorted_word] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in word_dict.values()))
    return anagram_pairs >= 96