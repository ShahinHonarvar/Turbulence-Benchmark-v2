from collections import defaultdict

def if_contains_anagrams(list_of_strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_dict = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_dict[sorted_string].append(string)
    anagram_pairs = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            anagram_pairs += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_pairs <= 78