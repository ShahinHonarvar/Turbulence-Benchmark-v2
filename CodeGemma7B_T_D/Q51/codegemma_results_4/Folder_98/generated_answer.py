from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for word in str_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(word) >= 3:
            anagram_dict[sorted_word].append(word)
    count = 0
    for anagram_group in anagram_dict.values():
        if len(anagram_group) > 1:
            count += len(anagram_group) // 2
    return count <= 46