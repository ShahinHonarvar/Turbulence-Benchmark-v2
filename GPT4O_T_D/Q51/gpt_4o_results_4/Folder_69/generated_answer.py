from collections import defaultdict

def if_contains_anagrams(words):

    def sorted_word(word):
        return ''.join(sorted(word.lower()))
    anagrams = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            anagrams[sorted_word(filter(str.isalpha, word))] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pair_count <= 58