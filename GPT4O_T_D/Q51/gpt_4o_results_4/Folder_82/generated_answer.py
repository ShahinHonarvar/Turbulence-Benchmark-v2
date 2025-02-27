from collections import defaultdict

def if_contains_anagrams(words):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    anagram_groups = defaultdict(list)
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            anagram_groups[canonical_form(word_lower)].append(word_lower)
    anagram_pairs = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            anagram_pairs += len(group) * (len(group) - 1) // 2
            if anagram_pairs > 40:
                return False
    return True