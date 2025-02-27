from collections import defaultdict

def if_contains_anagrams(words):

    def normalized(word):
        return ''.join(sorted(word.lower()))
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagram_groups[normalized(word)].append(word)
    anagram_pairs = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            n = len(group)
            anagram_pairs += n * (n - 1) // 2
            if anagram_pairs > 49:
                return False
    return True