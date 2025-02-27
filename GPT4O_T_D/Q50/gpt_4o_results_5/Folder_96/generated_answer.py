from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word)).lower()
    anagram_count = 0
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagram_groups[normalize(word)].append(word)
    for group in anagram_groups.values():
        n = len(group)
        if n >= 2:
            anagram_count += n * (n - 1) // 2
            if anagram_count >= 98:
                return True
    return False