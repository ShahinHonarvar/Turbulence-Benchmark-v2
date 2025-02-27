def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    second_largest = None
    largest = float('-inf')
    for index in range(13, 69):
        if num_list[index] > largest:
            second_largest = largest
            largest = num_list[index]
        elif num_list[index] > second_largest and num_list[index] < largest:
            second_largest = num_list[index]
    return second_largest