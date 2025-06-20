from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for s in string_list:
        cleaned_s = ''.join(filter(str.isalpha, s.lower()))
        if len(cleaned_s) >= 3:
            sorted_s = ''.join(sorted(cleaned_s))
            anagram_dict[sorted_s].append(cleaned_s)
    for anagrams in anagram_dict.values():
        anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
        if anagram_count > 11:
            return False
    return True