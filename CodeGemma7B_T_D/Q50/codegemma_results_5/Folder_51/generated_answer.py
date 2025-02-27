from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    count = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) >= 3:
            count += len(anagrams) - 2
    return count >= 39