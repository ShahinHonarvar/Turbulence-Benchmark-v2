from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s))
    anagram_map = defaultdict(int)
    for word in strings:
        if len(word) < 3:
            continue
        word_lower = word.lower()
        form = canonical_form(word_lower)
        anagram_map[form] += 1
    anagram_pairs = 0
    for count in anagram_map.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 3