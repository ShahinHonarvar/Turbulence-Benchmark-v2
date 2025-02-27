from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            anagram_key = sorted_string(word)
            anagram_map[anagram_key] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_map.values()))
    return anagram_pairs >= 5