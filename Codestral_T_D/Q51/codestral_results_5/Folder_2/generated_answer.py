from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(word_list):
    anagram_map = defaultdict(list)
    for word in word_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_map[sorted_word].append(word)
    anagram_pairs = sum((len(list(combinations(words, 2))) for words in anagram_map.values() if len(words) > 1))
    return anagram_pairs <= 81