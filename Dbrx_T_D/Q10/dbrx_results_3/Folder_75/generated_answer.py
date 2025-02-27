def all_odd_ints_exclusive(int_list):
    odd_ints = []
    for i in range(20, 36):
        if i >= len(int_list):
            break
        num = int_list[i]
        if num % 2 != 0:
            odd_ints.append(num)
    return odd_ints