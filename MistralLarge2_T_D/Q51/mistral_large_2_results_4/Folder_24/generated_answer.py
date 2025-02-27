from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagrams.values()))
    return pairs <= 96