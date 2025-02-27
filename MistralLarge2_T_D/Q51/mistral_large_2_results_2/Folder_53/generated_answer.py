from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_pairs = set()
    word_dict = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        for existing_word in word_dict[sorted_word]:
            anagram_pairs.add(tuple(sorted([existing_word, word])))
        word_dict[sorted_word].append(word)
    return len(anagram_pairs) <= 8