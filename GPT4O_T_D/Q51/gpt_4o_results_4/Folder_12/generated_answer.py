from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            anagram_groups[normalized].append(word)
    count = 0
    for group in anagram_groups.values():
        n = len(group)
        if n >= 2:
            count += n * (n - 1) // 2
        if count > 92:
            return False
    return True