from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word] += 1
    count = 0
    for key in anagrams:
        pairs = anagrams[key] * (anagrams[key] - 1) // 2
        count += pairs
        if count >= 61:
            return True
    return False