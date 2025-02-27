def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    second_largest = None
    largest = None
    for i in range(52, 72):
        if largest is None or numbers_list[i] > largest:
            second_largest = largest
            largest = numbers_list[i]
        elif largest is not None and second_largest is None and (numbers_list[i] < largest):
            second_largest = numbers_list[i]
        elif second_largest is not None and numbers_list[i] > second_largest and (numbers_list[i] < largest):
            second_largest = numbers_list[i]
    return second_largest