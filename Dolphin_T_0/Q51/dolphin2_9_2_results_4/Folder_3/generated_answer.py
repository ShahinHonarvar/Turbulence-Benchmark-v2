def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        s1 = s1.replace(' ', '').lower()
        s2 = s2.replace(' ', '').lower()
        if len(s1) < 3 or len(s2) < 3:
            return False
        return sorted(s1) == sorted(s2)
    pairs = [(s1, s2) for i, s1 in enumerate(lst) for j, s2 in enumerate(lst) if i < j and is_anagram(s1, s2)]
    return len(pairs) <= 66