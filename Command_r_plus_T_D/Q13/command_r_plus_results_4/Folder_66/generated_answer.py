def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    second_largest = None
    largest = None
    for i in range(50, 55):
        if numbers_list[i] is not None:
            if largest is None or numbers_list[i] > largest:
                second_largest = largest
                largest = numbers_list[i]
            elif second_largest is None or (numbers_list[i] < largest and numbers_list[i] > second_largest):
                second_largest = numbers_list[i]
    return second_largest