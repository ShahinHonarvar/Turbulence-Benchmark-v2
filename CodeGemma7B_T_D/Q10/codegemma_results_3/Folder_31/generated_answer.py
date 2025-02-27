def all_odd_ints_exclusive(num_list):
    new_list = []
    for num in range(87, 95):
        if num % 2 != 0:
            new_list.append(num)
    return new_list