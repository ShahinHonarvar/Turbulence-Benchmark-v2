from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = defaultdict(int)
    pairs = 0
    for word in strings:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_count[normalized_word] += 1
    for count in anagram_count.values():
        if count > 1:
            pairs += count * (count - 1) // 2
    return pairs >= 108