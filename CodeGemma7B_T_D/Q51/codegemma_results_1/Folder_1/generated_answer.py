from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_map = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_map:
            anagram_map[sorted_word].append(word)
        else:
            anagram_map[sorted_word] = [word]
    num_anagrams = 0
    for anagrams in anagram_map.values():
        num_anagrams += len(anagrams) * (len(anagrams) - 1) // 2
    return num_anagrams <= 30