from collections import Counter

def if_contains_anagrams(lst):
    anagram_counts = {}
    pair_count = 0
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_counts:
                pair_count += anagram_counts[sorted_word]
                anagram_counts[sorted_word] += 1
            else:
                anagram_counts[sorted_word] = 1
            if pair_count > 392:
                return False
    return True