from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_map = defaultdict(list)
    for word in string_list:
        word = ''.join(filter(str.isalpha, word.lower()))
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
    for anagrams in anagram_map.values():
        if len(anagrams) > 1:
            anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count <= 73