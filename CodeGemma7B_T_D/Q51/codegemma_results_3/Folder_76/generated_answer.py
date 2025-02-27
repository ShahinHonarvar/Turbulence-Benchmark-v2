def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    pairs = []
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]):
                pairs.append((str_list[i], str_list[j]))
    if len(pairs) <= 91:
        return True
    else:
        return False