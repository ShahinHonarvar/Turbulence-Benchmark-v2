from collections import defaultdict

def if_contains_anagrams(words):
    anagram_counts = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_counts[sorted_word] += 1
    count = 0
    for val in anagram_counts.values():
        if val > 1:
            count += val * (val - 1) // 2
            if count >= 40:
                return True
    return False