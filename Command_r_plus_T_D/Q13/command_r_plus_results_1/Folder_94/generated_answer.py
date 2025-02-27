def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sub_array = numbers[28:41]
    if len(sub_array) < 2:
        return None
    sub_array.sort()
    return sub_array[-2]