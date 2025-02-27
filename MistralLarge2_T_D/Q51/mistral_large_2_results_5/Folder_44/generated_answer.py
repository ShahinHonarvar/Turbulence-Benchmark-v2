from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(set)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].add(word)
    anagram_pairs = 0
    for group in anagram_dict.values():
        if len(group) > 1:
            anagram_pairs += len(group) * (len(group) - 1) // 2
            if anagram_pairs > 75:
                return False
    return True