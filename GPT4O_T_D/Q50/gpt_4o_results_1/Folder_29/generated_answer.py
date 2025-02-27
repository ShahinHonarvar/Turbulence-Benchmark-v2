from collections import defaultdict

def if_contains_anagrams(strings):

    def normalized(word):
        return ''.join(sorted(word.lower()))
    anagram_groups = defaultdict(int)
    for word in strings:
        if len(word) >= 3:
            key = normalized(word)
            anagram_groups[key] += 1
    count_pairs = 0
    for count in anagram_groups.values():
        if count > 1:
            count_pairs += count * (count - 1) // 2
    return count_pairs >= 35