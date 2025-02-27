from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for word in strings:
        if len(word) >= 3:
            sorted_word = normalize(word)
            anagram_count[sorted_word] += 1
    pairs = 0
    for count in anagram_count.values():
        if count > 1:
            pairs += count * (count - 1) // 2
    return pairs >= 411