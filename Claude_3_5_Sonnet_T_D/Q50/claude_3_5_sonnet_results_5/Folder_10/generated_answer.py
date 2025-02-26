from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for word in string_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_dict.values()))
    return anagram_pairs >= 52