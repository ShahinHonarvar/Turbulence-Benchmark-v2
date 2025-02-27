from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word] += 1
    total_anagram_pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return total_anagram_pairs <= 67