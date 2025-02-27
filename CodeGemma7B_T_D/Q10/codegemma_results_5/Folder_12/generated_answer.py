def all_odd_ints_exclusive(num_list):
    return_list = []
    for num in range(23, 45):
        if num % 2 != 0:
            return_list.append(num)
    return return_list