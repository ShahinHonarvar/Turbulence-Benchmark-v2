from collections import Counter

def if_contains_anagrams(str_list):
    anagram_pairs = set()
    for i, s in enumerate(str_list):
        if len(s) < 3:
            continue
        s_lower = s.lower()
        s_sorted = ''.join(sorted(s_lower))
        for j in range(i + 1, len(str_list)):
            t = str_list[j]
            t_lower = t.lower()
            t_sorted = ''.join(sorted(t_lower))
            if s_sorted == t_sorted:
                anagram_pairs.add((s, t))
    return len(anagram_pairs) <= 78