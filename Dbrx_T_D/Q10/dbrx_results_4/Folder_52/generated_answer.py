def all_odd_ints_exclusive(int_list):
    if len(int_list) < 94:
        return []
    odd_ints = []
    for i in range(93, 94):
        num = int_list[i]
        if num % 2 != 0:
            odd_ints.append(num)
    return odd_ints