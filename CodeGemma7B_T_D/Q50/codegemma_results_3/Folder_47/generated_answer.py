def if_contains_anagrams(str_list):
    str_list2 = []
    for s in str_list:
        str_list2.append(''.join(sorted(s.lower())))
    str_list2.sort()
    pairs = 0
    for i in range(len(str_list2)):
        for j in range(i + 1, min(i + 48, len(str_list2))):
            if str_list2[i] == str_list2[j]:
                pairs += 1
    return pairs >= 47