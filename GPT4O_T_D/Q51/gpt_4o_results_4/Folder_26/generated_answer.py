from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    word_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            norm_word = normalize(word)
            word_dict[norm_word].append(word)
    for group in word_dict.values():
        if len(group) > 1:
            possible_pairs = len(group) * (len(group) - 1) // 2
            anagram_count += possible_pairs
            if anagram_count > 35:
                return False
    return True