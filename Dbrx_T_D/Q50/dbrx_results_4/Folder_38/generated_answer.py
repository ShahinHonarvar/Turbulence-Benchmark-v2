import itertools

def if_contains_anagrams(string_list):
    anagrams_dict = {}
    for word in string_list:
        if len(word) >= 3:
            sorted_word = tuple(sorted(word.lower()))
            if sorted_word not in anagrams_dict:
                anagrams_dict[sorted_word] = set()
            anagrams_dict[sorted_word].add(word)
    total_anagram_pairs = sum((len(pair) * (len(pair) - 1) // 2 for pair in anagrams_dict.values()))
    return total_anagram_pairs >= 24