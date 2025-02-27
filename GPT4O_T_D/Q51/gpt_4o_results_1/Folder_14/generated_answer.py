from collections import defaultdict

def if_contains_anagrams(str_list):

    def sorted_str(s):
        return ''.join(sorted(s))
    anagrams = defaultdict(set)
    for word in str_list:
        normalized_word = ''.join(filter(str.isalpha, word)).lower()
        if len(normalized_word) >= 3:
            key = sorted_str(normalized_word)
            anagrams[key].add(normalized_word)
    pairs_count = sum((len(words) * (len(words) - 1) // 2 for words in anagrams.values()))
    return pairs_count <= 474