from collections import defaultdict

def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        anagram_dict[sorted_str].append(string)
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1 and len(anagram_dict[key][0]) >= 3:
            anagram_count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_count <= 15