def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in num_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return None if second_largest == float('-inf') else second_largest