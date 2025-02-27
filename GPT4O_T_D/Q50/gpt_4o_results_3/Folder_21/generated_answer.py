from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(int)
    count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word] += 1
    for val in anagrams.values():
        if val > 1:
            count += val * (val - 1) // 2
        if count >= 136:
            return True
    return False