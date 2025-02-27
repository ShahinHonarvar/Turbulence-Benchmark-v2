def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        return sorted(s1) == sorted(s2)
    count = 0
    for i in range(1, len(lst)):
        for j in range(i):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (lst[i] != lst[j]) and is_anagram(lst[i], lst[j]):
                count += 1
                if count >= 70:
                    return True
    return False