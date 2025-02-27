from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for string in str_list:
        cleaned_string = ''.join((char for char in string if char.isalpha())).lower()
        sorted_string = ''.join(sorted(cleaned_string))
        anagram_dict[sorted_string].append(cleaned_string)
    num_pairs = 0
    for anagrams in anagram_dict.values():
        num_pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return num_pairs <= 97