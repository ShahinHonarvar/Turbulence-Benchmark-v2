def if_contains_anagrams(str_list):
    str_dic = {}
    for st in str_list:
        st = st.lower()
        sorted_st = ''.join(sorted(st))
        if len(st) >= 3 and sorted_st in str_dic:
            str_dic[sorted_st] += 1
        elif len(st) >= 3:
            str_dic[sorted_st] = 1
    return sum((value >= 2 for value in str_dic.values())) <= 43