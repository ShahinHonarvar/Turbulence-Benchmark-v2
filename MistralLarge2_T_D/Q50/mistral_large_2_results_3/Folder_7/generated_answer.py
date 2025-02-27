from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    count_pairs = sum((1 for pair in anagrams.values() if len(pair) > 1))
    return count_pairs >= 178