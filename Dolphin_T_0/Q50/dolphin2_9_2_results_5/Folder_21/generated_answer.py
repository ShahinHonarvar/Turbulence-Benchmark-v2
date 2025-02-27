from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    counter = defaultdict(int)
    for s1, s2 in zip(lst, lst[1:]):
        if is_anagram(s1, s2) and len(s1) >= 3:
            counter[s1] += 1
    return counter and sum(counter.values()) >= 136