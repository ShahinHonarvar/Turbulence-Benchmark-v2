from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word] += 1
    count_pairs = sum((count * (count - 1) // 2 for count in anagrams.values() if count > 1))
    return count_pairs <= 30