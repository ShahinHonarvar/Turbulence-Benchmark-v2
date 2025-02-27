from collections import defaultdict

def if_contains_anagrams(words):

    def normalize_word(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    seen = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            normalized = normalize_word(word)
            anagram_count += seen[normalized]
            seen[normalized] += 1
    return anagram_count <= 89