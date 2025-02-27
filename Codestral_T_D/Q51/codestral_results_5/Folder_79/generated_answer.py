from collections import Counter

def if_contains_anagrams(str_list):
    anagrams = {}
    for s in str_list:
        lower_s = s.lower()
        if len(lower_s) >= 3:
            sorted_s = ''.join(sorted(lower_s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = 1
            else:
                anagrams[sorted_s] += 1
    count = 0
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 173