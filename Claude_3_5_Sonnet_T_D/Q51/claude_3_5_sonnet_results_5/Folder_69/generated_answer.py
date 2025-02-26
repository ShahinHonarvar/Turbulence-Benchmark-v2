from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = {}
    for s in string_list:
        cleaned_s = ''.join(filter(str.isalpha, s.lower()))
        if len(cleaned_s) < 3:
            continue
        sorted_s = ''.join(sorted(cleaned_s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(cleaned_s)
        else:
            anagram_dict[sorted_s] = [cleaned_s]
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
        if anagram_count > 58:
            return False
    return True