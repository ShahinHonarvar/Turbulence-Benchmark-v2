from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_count[sorted_word].append(word)
    pairs_count = sum((len(group) // 2 for group in anagram_count.values() if len(group) >= 2))
    return pairs_count >= 22