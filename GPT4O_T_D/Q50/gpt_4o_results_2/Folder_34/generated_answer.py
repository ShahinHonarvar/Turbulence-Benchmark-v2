from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word)
    anagram_pairs = sum((len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2 for key in anagram_dict))
    return anagram_pairs >= 25