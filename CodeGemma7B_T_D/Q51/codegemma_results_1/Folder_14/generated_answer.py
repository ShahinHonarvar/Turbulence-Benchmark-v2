def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    pairs = 0
    i = 0
    j = 1
    while i < len(str_list) - 1:
        while j < len(str_list):
            if sorted(str_list[i]) == sorted(str_list[j]):
                pairs += 1
            j += 1
        i += 1
        j = i + 1
    return pairs <= 474