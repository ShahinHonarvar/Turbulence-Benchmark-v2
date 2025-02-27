from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = defaultdict(int)
    for word in strings:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_counts[normalized_word] += 1
    anagram_pairs = 0
    for count in anagram_counts.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs >= 144:
                return True
    return False