from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = defaultdict(int)
    for word in words:
        if len(word) < 3:
            continue
        normalized = normalize(word)
        anagram_count[normalized] += 1
    count_pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return count_pairs <= 92