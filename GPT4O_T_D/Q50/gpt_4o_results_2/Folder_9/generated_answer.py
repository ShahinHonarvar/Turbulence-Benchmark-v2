from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_groups[sorted_word] += 1
    pairs = 0
    for count in anagram_groups.values():
        if count > 1:
            pairs += count * (count - 1) // 2
        if pairs >= 66:
            return True
    return False