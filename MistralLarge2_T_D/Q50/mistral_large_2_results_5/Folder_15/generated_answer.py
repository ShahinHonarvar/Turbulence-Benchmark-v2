from collections import defaultdict

def if_contains_anagrams(words):
    anagram_counts = defaultdict(int)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_counts[sorted_word] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_counts.values() if count > 1))
    return pairs_count >= 4