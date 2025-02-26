from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    anagram_count = 0
    for s in string_list:
        sorted_s = ''.join(sorted(filter(str.isalpha, s.lower())))
        if len(sorted_s) >= 3:
            anagram_dict[sorted_s].append(s)
    for words in anagram_dict.values():
        if len(words) > 1:
            anagram_count += len(words) * (len(words) - 1) // 2
            if anagram_count > 14:
                return False
    return True