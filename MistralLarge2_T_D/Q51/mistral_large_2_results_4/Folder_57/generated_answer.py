from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    length_filtered_lst = [s for s in lst if len(s) >= 3]
    checked_pairs = set()
    for i in range(len(length_filtered_lst)):
        for j in range(i + 1, len(length_filtered_lst)):
            if (i, j) not in checked_pairs and (j, i) not in checked_pairs:
                if is_anagram(length_filtered_lst[i], length_filtered_lst[j]):
                    anagram_count += 1
                    checked_pairs.add((i, j))
                    checked_pairs.add((j, i))
    return anagram_count <= 74