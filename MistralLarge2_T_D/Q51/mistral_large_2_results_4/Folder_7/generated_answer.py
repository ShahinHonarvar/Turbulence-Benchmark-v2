from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = 0
    checked_pairs = set()
    for str1, str2 in combinations(strings, 2):
        if len(str1) >= 3 and len(str2) >= 3:
            sorted_str1 = tuple(sorted(str1.lower()))
            sorted_str2 = tuple(sorted(str2.lower()))
            if sorted_str1 == sorted_str2:
                if (str1, str2) not in checked_pairs and (str2, str1) not in checked_pairs:
                    anagram_pairs += 1
                    checked_pairs.add((str1, str2))
                    checked_pairs.add((str2, str1))
    return anagram_pairs <= 445