def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    second_largest = None
    largest = float('-inf')
    for i in range(13, 69):
        if num_list[i] > largest:
            second_largest = largest
            largest = num_list[i]
        elif num_list[i] > second_largest and num_list[i] != largest:
            second_largest = num_list[i]
    return second_largest