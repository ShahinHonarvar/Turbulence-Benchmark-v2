from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = sorted_chars(word)
            anagram_groups[sorted_word] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_groups.values()))
    return pairs_count >= 88