from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = {}
    for s in string_list:
        cleaned_s = ''.join((char.lower() for char in s if char.isalpha()))
        if len(cleaned_s) < 3:
            continue
        sorted_s = ''.join(sorted(cleaned_s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s)
            if len(anagram_dict[sorted_s]) == 2:
                anagram_count += 1
        else:
            anagram_dict[sorted_s] = [s]
        if anagram_count > 257:
            return False
    return True