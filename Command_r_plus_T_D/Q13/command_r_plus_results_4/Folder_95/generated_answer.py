def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sub_list = numbers[81:87]
    if len(sub_list) < 2:
        return None
    second_largest = None
    largest = sub_list[0]
    for num in sub_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest