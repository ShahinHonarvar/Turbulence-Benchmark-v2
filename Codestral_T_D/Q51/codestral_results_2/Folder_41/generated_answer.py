from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word)
    anagram_count = 0
    for key in anagram_dict:
        length = len(anagram_dict[key])
        anagram_count += length * (length - 1) // 2
    return anagram_count <= 52