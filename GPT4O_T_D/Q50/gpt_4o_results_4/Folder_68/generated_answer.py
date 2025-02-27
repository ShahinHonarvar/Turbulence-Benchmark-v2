from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for words in anagram_dict.values():
        count = len(words)
        if count >= 2:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 9