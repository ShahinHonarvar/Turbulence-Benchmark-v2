from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    anagram_pairs = set()
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            anagram_pairs.add(sorted_word)
    for pair in anagram_pairs:
        if len(pair) < 3:
            anagram_pairs.remove(pair)
    count = 0
    for pair in anagram_pairs:
        for other_pair in anagram_pairs:
            if other_pair == pair and anagram_pairs.count(other_pair) > 1:
                count += 1
    if count <= 38:
        return True
    else:
        return False