from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    count = 0
    for group in anagrams.values():
        if len(group) >= 2:
            count += len(group) * (len(group) - 1) // 2
    return count <= 21