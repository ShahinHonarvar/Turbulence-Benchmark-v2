def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    second_largest = None
    largest = None
    for i in range(209, 557):
        num = numbers_list[i]
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or (num > second_largest and num < largest):
            second_largest = num
    return second_largest