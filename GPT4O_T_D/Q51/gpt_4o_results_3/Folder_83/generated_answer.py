from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    normalized_lst = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    n = len(normalized_lst)
    for i in range(n):
        for j in range(i + 1, n):
            if normalized_lst[i] == normalized_lst[j]:
                anagram_pairs += 1
                if anagram_pairs > 19:
                    return False
    return True