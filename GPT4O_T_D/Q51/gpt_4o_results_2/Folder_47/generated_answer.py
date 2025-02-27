from collections import Counter

def if_contains_anagrams(words):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    valid_words = [canonical_form(word) for word in words if len(word) >= 3]
    anagram_map = Counter(valid_words)
    count = 0
    for freq in anagram_map.values():
        if freq > 1:
            count += freq * (freq - 1) // 2
        if count > 366:
            return False
    return True