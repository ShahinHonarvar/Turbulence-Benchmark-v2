def all_odd_ints_inclusive(num_list):
    odd_list = []
    for i in range(22, 89):
        if num_list[i] % 2 != 0:
            odd_list.append(num_list[i])
    if len(odd_list) == 0:
        return []
    else:
        return odd_list