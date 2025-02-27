from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_count[sorted_word].append(word)
    anagram_pairs = sum((1 for group in anagram_count.values() if len(group) > 1))
    return anagram_pairs <= 318