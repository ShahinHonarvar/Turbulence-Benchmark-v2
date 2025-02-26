from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_map = defaultdict(list)
    for word in string_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_map.values()))
    return anagram_pairs >= 44