from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = {}
    for s in string_list:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s)
            else:
                anagram_dict[sorted_s] = [s]
    for words in anagram_dict.values():
        if len(words) > 1:
            anagram_count += len(words) * (len(words) - 1) // 2
    return anagram_count >= 81