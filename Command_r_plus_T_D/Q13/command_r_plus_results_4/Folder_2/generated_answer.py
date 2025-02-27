def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 40:
        return None
    second_largest = None
    for i in range(15, 40):
        if second_largest is None or num_list[i] > second_largest:
            second_largest = num_list[i]
    for i in range(15, 40):
        if num_list[i] > second_largest:
            second_largest = num_list[i]
    return second_largest