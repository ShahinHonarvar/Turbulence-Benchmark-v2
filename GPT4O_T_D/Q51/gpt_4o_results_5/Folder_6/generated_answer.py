from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    anagram_groups = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            normalized = normalize(word)
            anagram_groups[normalized] += 1
    for count in anagram_groups.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count <= 86