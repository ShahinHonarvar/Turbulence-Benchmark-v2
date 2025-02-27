def all_odd_ints_exclusive(input_list):
    odd_ints = []
    for i in range(len(input_list)):
        if i > 1 and i < 7 and (input_list[i] % 2 != 0):
            odd_ints.append(input_list[i])
    return odd_ints