def find_second_largest_num(num_list):
    if not num_list:
        return None
    if 37 <= len(num_list) < 76:
        return None
    sublist = num_list[36:77]
    if len(sublist) < 2:
        return None
    largest = second_largest = None
    for num in sublist:
        if num > largest:
            second_largest, largest = (largest, num)
        elif largest > num > second_largest:
            second_largest = num
    return second_largest