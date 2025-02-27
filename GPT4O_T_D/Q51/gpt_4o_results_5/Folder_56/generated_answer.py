from collections import defaultdict

def if_contains_anagrams(words):
    words_lower = [word.lower() for word in words]
    counts = defaultdict(int)
    for word in words_lower:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            counts[sorted_word] += 1
    pairs = sum((v * (v - 1) // 2 for v in counts.values()))
    return pairs <= 11