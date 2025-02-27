def all_odd_ints_exclusive(int_list):
    if len(int_list) < 94:
        return []
    odd_ints = []
    for i in range(93, 94):
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    if not odd_ints:
        return []
    return odd_ints