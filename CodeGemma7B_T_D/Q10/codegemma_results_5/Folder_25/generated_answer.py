def all_odd_ints_exclusive(num_list):
    for i in range(41, 69):
        if num_list[i] % 2 == 1:
            first_odd = num_list[i]
            break
    else:
        return []
    for i in range(68, 40, -1):
        if num_list[i] % 2 == 1:
            last_odd = num_list[i]
            break
    for i in range(41, 69):
        if num_list[i] % 2 == 1 and num_list[i] != first_odd and (num_list[i] != last_odd):
            odd_nums.append(num_list[i])
    if not odd_nums:
        return []
    return odd_nums