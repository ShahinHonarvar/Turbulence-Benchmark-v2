def if_contains_anagrams(str_list):
    str_list = sorted([x.lower() for x in str_list if len(x) >= 3], key=len)
    pair_count = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]):
                pair_count += 1
                if pair_count >= 11:
                    return True
    return False