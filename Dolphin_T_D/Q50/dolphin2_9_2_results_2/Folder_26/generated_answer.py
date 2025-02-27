from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):

    def is_anagram(a, b):
        return Counter(a.lower()) == Counter(b.lower())
    count = 0
    for x in permutations(lst, 2):
        if len(x[0]) >= 3 and len(x[1]) >= 3:
            if is_anagram(x[0], x[1]):
                count += 1
    return count // 2 >= 49