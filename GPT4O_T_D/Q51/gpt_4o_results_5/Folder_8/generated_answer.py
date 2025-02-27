from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_map = defaultdict(list)
    cnt = 0
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            key = ''.join(sorted(word))
            anagram_map[key].append(word)
    for words in anagram_map.values():
        n = len(words)
        cnt += n * (n - 1) // 2
        if cnt > 68:
            return False
    return True