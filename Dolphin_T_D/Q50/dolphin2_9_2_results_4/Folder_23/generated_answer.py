def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        return sorted(s1) == sorted(s2) and len(s1) >= 3 and (len(s2) >= 3)
    c = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                c += 1
    return c >= 67