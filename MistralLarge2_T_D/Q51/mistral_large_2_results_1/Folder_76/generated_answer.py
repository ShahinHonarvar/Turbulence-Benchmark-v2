from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    checked_pairs = set()
    len_lst = len(lst)
    for i in range(len_lst):
        for j in range(i + 1, len_lst):
            if (i, j) not in checked_pairs and (j, i) not in checked_pairs:
                if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                    anagram_count += 1
                    if anagram_count > 91:
                        return False
                checked_pairs.add((i, j))
                checked_pairs.add((j, i))
    return True