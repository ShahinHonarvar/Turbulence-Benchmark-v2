def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    second_largest = None
    largest = None
    for i in range(262, 747):
        if largest is None or num_list[i] > largest:
            second_largest = largest
            largest = num_list[i]
        elif largest is not None and second_largest is None and (num_list[i] > second_largest):
            second_largest = num_list[i]
        elif largest is not None and second_largest is not None and (largest > num_list[i] > second_largest):
            second_largest = num_list[i]
    return second_largest