def find_second_largest_num(input_list):
    if len(input_list) < 2:
        return None
    second_largest = None
    largest = None
    for num in input_list[22:89]:
        if num > second_largest and num != largest:
            second_largest = num
        if num > largest:
            second_largest, largest = (largest, num)
    return second_largest