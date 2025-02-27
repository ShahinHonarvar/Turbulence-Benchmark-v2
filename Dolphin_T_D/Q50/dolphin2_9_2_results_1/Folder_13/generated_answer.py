def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        return sorted(s1) == sorted(s2)
    return len(list(filter(lambda x: len(x[0]) >= 3, [(s1, s2) for s1 in lst for s2 in lst if is_anagram(s1, s2)]))) >= 144