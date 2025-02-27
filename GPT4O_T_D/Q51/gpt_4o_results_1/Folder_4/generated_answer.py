from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(filter(str.isalpha, word.lower())))
        if len(sorted_word) >= 3:
            anagrams[sorted_word].append(word)
    pairs_count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return pairs_count <= 84