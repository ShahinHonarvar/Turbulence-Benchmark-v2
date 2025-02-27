def all_odd_ints_exclusive(int_list):
    odd_ints = []
    for i in range(94, 95):
        if i >= len(int_list) or i < 0:
            return odd_ints
        n = int_list[i]
        if n % 2 != 0:
            odd_ints.append(n)
    return odd_ints