from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for word in string_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word].append(word)
    for anagram_group in anagram_dict.values():
        if len(anagram_group) > 1:
            anagram_count += len(anagram_group) * (len(anagram_group) - 1) // 2
    return anagram_count >= 35