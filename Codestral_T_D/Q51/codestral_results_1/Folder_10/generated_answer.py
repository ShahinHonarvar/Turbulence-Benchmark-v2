from collections import Counter

def if_contains_anagrams(lst):
    anagram_groups = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagram_groups:
                anagram_groups[sorted_word] = []
            anagram_groups[sorted_word].append(word)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()))
    return anagram_pairs <= 21