def if_contains_anagrams(lst):

    def sort_str(s):
        return ''.join(sorted(s.lower()))
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            s1 = sort_str(lst[i])
            s2 = sort_str(lst[j])
            if len(s1) >= 3 and s1 == s2:
                pairs += 1
    return pairs >= 61