def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    second_largest = None
    largest = float('-inf')
    for index in range(50, 55):
        if numbers_list[index] > largest:
            second_largest = largest
            largest = numbers_list[index]
        elif numbers_list[index] > second_largest and numbers_list[index] != largest:
            second_largest = numbers_list[index]
    return second_largest