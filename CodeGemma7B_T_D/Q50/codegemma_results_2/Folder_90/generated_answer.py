def if_contains_anagrams(str_list):
    str_list = [i.lower() for i in str_list]
    pair_count = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]) and (len(str_list[i]) >= 3 and len(str_list[j]) >= 3):
                pair_count += 1
    return pair_count >= 177