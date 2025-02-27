from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_pairs_count = sum((len(group) - 1 for group in anagram_dict.values() if len(group) > 1))
    return anagram_pairs_count <= 47