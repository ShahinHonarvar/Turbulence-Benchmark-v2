def if_contains_anagrams(lst):
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            s1 = ''.join(filter(str.isalpha, lst[i].lower()))
            s2 = ''.join(filter(str.isalpha, lst[j].lower()))
            if sorted(s1) == sorted(s2) and len(s1) >= 3:
                anagrams_count += 1
    return anagrams_count <= 445