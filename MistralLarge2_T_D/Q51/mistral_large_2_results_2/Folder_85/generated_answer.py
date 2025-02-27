def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and are_anagrams(lst[i], lst[j]):
                count += 1
                if count > 276:
                    return False
    return True