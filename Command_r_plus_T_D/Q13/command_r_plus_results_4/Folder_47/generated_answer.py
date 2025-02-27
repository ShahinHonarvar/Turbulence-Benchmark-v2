def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    target_range = num_list[37:77]
    if len(target_range) < 2:
        return None
    second_largest = None
    largest = float('-inf')
    for num in target_range:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest