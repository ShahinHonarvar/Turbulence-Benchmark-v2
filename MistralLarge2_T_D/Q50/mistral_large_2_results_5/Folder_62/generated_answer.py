from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(string):
        return ''.join(sorted(string.lower()))
    anagram_count = defaultdict(int)
    pairs_count = 0
    for word in lst:
        if len(word) >= 3:
            norm_word = normalize(word)
            anagram_count[norm_word] += 1
            pairs_count += anagram_count[norm_word] - 1
    return pairs_count >= 43