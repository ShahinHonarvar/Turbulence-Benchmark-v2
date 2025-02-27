from collections import Counter

def if_contains_anagrams(str_list):
    anagrams = Counter((''.join(sorted(str.lower())) for str in str_list if len(str) >= 3)).values()
    return sum((a > 1 for a in anagrams)) <= 464