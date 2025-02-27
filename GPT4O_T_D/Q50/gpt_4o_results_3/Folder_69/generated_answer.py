from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagram_key = normalize(word)
            anagram_dict[anagram_key].append(word)
    pair_count = sum((len(group) * (len(group) - 1) // 2 for group in anagram_dict.values()))
    return pair_count >= 188