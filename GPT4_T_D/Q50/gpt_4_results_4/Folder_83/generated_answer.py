from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    pairs = 0
    for word_list in anagrams.values():
        pairs += len(word_list) * (len(word_list) - 1) // 2
    return pairs >= 48