def gcf_two_nums(a_list):
    a = a_list[69]
    b = a_list[41]
    a_set = set(range(1, a + 1))
    b_set = set(range(1, b + 1))
    gcf = max(a_set.intersection(b_set))
    return gcf