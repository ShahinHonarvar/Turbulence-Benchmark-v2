def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sub_array = numbers[28:33]
    sub_array.sort()
    if len(sub_array) < 2:
        return None
    else:
        return sub_array[-2]