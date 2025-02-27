from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_groups = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_groups[normalized_word] += 1
    count_pairs = 0
    for count in anagram_groups.values():
        if count > 1:
            count_pairs += count * (count - 1) // 2
            if count_pairs > 15:
                return False
    return count_pairs <= 15