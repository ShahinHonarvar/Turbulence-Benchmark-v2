def all_odd_ints_exclusive(input_list):
    odd_ints = []
    for i in range(86, 89):
        if i < len(input_list) and input_list[i] % 2 != 0:
            odd_ints.append(input_list[i])
    return odd_ints