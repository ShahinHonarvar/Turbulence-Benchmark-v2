from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_groups = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_groups[normalized_word].append(word)
    anagram_pairs = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
        if anagram_pairs > 58:
            return False
    return True