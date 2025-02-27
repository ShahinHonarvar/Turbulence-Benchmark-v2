def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    res = {}
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3 and (len(lst[j]) >= 3):
                try:
                    res[i] += 1
                except KeyError:
                    res[i] = 1
                try:
                    res[j] += 1
                except KeyError:
                    res[j] = 1
    return max(res.values()) <= 60