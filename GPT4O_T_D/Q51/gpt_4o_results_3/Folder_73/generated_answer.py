from collections import defaultdict

def if_contains_anagrams(words):

    def normalize_word(word):
        return ''.join(sorted(word.lower()))
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            normalized = normalize_word(word)
            anagram_groups[normalized].append(word)
    anagram_pairs = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
            if anagram_pairs > 279:
                return False
    return True