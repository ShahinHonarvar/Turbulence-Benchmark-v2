from collections import defaultdict

def if_contains_anagrams(words):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    anagram_count = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            form = canonical_form(word)
            anagram_count[form] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return anagram_pairs <= 97