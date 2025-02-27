def all_odd_ints_inclusive(input_list):
    odd_ints = []
    for i in range(max(90, 0), min(len(input_list), 201)):
        if input_list[i] % 2 != 0:
            odd_ints.append(input_list[i])
    return odd_ints