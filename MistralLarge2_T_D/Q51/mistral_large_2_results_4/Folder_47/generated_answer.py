from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word].append(word)
    count = 0
    for group in anagrams.values():
        if len(group) > 1:
            count += len(group) - 1
    return count <= 366