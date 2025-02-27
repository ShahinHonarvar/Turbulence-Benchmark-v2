from collections import Counter

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_groups = Counter()
    for word in words:
        if len(word) >= 3:
            anagram_groups[normalize(word)] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_groups.values()))
    return pairs_count >= 89