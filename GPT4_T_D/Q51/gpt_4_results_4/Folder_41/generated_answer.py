from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    word_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            word_dict[''.join(sorted(word.lower()))].append(word)
    anagram_pairs = sum((len(values) * (len(values) - 1) // 2 for values in word_dict.values()))
    return anagram_pairs <= 52