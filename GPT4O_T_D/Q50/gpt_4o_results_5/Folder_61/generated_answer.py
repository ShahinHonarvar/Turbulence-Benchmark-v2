from collections import defaultdict

def if_contains_anagrams(lst):
    pairs = 0
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    for words in anagram_dict.values():
        n = len(words)
        if n > 1:
            pairs += n * (n - 1) // 2
        if pairs >= 8:
            return True
    return False