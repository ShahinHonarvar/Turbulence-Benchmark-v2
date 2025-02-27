def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [''.join(sorted(s)) for s in str_list]
    str_list.sort()
    pairs = 0
    for i in range(len(str_list)):
        for j in range(i + 2, len(str_list)):
            if str_list[i] == str_list[j]:
                pairs += 1
    return pairs <= 131