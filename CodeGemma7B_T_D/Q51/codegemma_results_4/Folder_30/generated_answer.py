from collections import Counter

def if_contains_anagrams(str_list):
    seen_anagrams = set()
    for string in str_list:
        key = tuple(sorted(Counter(string.lower()).items()))
        if key in seen_anagrams:
            return False
        seen_anagrams.add(key)
    return True