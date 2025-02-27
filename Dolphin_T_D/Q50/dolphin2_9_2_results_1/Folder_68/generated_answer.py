def if_contains_anagrams(lst):

    def are_anagrams(a, b):
        return sorted(a.lower()) == sorted(b.lower()) and len(a) >= 3 and (len(b) >= 3)
    cnt = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if are_anagrams(lst[i], lst[j]):
                cnt += 1
                if cnt >= 9:
                    return True
    return False