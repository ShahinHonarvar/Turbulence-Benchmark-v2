from collections import Counter

def if_contains_anagrams(lst):
    anagram_counts = Counter()
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_counts[sorted_word] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 475