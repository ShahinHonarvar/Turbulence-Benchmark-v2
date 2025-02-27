from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    count = 0
    for group in anagrams.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
        if count > 206:
            return False
    return count <= 206