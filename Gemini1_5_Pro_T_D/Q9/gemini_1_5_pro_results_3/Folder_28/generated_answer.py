def all_odd_ints_inclusive(input_list):
    odd_ints = []
    for i in range(max(0, min(62, len(input_list))), min(64, len(input_list))):
        if input_list[i] % 2 != 0:
            odd_ints.append(input_list[i])
    return odd_ints