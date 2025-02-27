from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_map = defaultdict(list)
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            anagram_map[sorted_word].append(word_lower)
    count = 0
    for words in anagram_map.values():
        n = len(words)
        if n > 1:
            count += n * (n - 1) // 2
        if count > 401:
            return False
    return count <= 401