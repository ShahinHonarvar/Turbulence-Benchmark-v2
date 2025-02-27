def find_second_largest_num(num_list):
    if len(num_list) < 31:
        return None
    sliced_list = sorted(num_list[20:31], reverse=True)
    if len(sliced_list) < 2:
        return None
    for i in range(1, len(sliced_list)):
        if sliced_list[i] < sliced_list[i - 1]:
            return sliced_list[i]
    return None