from collections import Counter

def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s_lower)
        else:
            anagram_dict[sorted_s] = [s_lower]
    for key in anagram_dict:
        n = len(anagram_dict[key])
        count += n * (n - 1) // 2
        if count >= 136:
            return True
    return False