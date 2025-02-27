from collections import Counter

def if_contains_anagrams(ls):

    def anagram(s):
        return Counter(s.lower()[1:])
    ana_dict = {}
    for s in ls:
        if len(s) >= 3:
            ana_dict.setdefault(anagram(s), []).append(s)
    count = 0
    for key in ana_dict:
        if len(ana_dict[key]) >= 2:
            count += 1
    return count <= 74