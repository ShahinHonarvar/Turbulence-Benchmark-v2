def if_contains_anagrams(lst):
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            s1 = ''.join(filter(str.isalpha, lst[i].lower()))
            s2 = ''.join(filter(str.isalpha, lst[j].lower()))
            if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2)):
                anagrams_count += 1
                if anagrams_count > 42:
                    return False
    return True