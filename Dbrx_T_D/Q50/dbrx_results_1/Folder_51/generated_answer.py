import string

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    count = 0
    for s in list_of_strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    for value in anagrams.values():
        if value > 1:
            count += value * (value - 1) // 2
    return count >= 39