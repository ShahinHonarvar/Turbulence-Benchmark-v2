from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    count = 0
    for pair in combinations(lst, 2):
        if is_anagram(pair[0], pair[1]) and len(pair[0]) >= 3 and (len(pair[1]) >= 3):
            count += 1
    return count >= 85