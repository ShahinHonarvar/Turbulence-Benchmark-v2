def if_contains_anagrams(lst):
    s_list = set()
    for s in lst:
        if len(s) >= 3:
            s_list.add(s.lower())
    count = 0
    for i in range(len(s_list) - 1):
        for j in range(i + 1, len(s_list)):
            if sorted(s_list[i]) == sorted(s_list[j]):
                count += 1
    if count >= 81:
        return True
    else:
        return False