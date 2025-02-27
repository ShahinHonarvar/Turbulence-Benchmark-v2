def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    res = {}
    for s1 in lst:
        if len(s1) >= 3:
            for s2 in lst:
                if s1 != s2 and len(s2) >= 3 and is_anagram(s1, s2):
                    if s1 in res:
                        if s2 not in res[s1]:
                            res[s1].append(s2)
                    else:
                        res[s1] = [s2]
    if len(res) >= 86:
        return True
    else:
        return False