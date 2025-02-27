def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    second_largest = None
    largest = float('-inf')
    for i in range(91, 100):
        if numbers_list[i] > largest:
            second_largest = largest
            largest = numbers_list[i]
        elif numbers_list[i] > second_largest and numbers_list[i] != largest:
            second_largest = numbers_list[i]
    return second_largest