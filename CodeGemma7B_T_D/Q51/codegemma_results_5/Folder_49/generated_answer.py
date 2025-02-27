from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_counts = defaultdict(int)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_counts[sorted_word] += 1
    anagram_pairs = sum((value // 2 for value in anagram_counts.values()))
    return anagram_pairs <= 10