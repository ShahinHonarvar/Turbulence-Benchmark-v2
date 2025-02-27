def all_odd_ints_inclusive(input_list):
    if len(input_list) < 89:
        return []
    odd_ints = []
    for i in range(75, 89):
        if input_list[i] % 2 != 0:
            odd_ints.append(input_list[i])
    return odd_ints