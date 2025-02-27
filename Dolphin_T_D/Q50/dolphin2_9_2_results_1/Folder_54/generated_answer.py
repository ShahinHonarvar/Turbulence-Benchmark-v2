from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    counter = Counter()
    for word in lst:
        if len(word) < 3:
            continue
        counter[tuple(sorted(word.lower()))] += 1
    return sum((v * (v - 1) // 2 >= 74 for v in counter.values())) >= 1