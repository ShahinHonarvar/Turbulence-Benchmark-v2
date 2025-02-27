from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        lower_word = ''.join(filter(str.isalpha, word)).lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            anagrams[sorted_word].append(lower_word)
    pair_count = 0
    for word_list in anagrams.values():
        n = len(word_list)
        if n > 1:
            pair_count += n * (n - 1) // 2
    return pair_count <= 77