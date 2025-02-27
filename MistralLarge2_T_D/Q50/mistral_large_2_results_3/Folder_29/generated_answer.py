from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_count[sorted_word].append(word)
    count = sum((len(lst) >= 2 for lst in anagram_count.values()))
    return count >= 35