from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())

    def get_permutations(s):
        return set(map(''.join, permutations(s.lower())))
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3 and (len(lst[j]) >= 3):
                count += 1
    return count <= 73