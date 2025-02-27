from collections import defaultdict

def if_contains_anagrams(strings_list):
    anagrams_dict = defaultdict(list)
    anagram_pairs_count = 0
    for string in strings_list:
        sorted_string = ''.join(sorted(string))
        anagrams_dict[sorted_string].append(string)
    for anagrams_list in anagrams_dict.values():
        if len(anagrams_list) >= 75:
            anagram_pairs_count += len(anagrams_list) * (len(anagrams_list) - 1) // 2
    return anagram_pairs_count >= 75