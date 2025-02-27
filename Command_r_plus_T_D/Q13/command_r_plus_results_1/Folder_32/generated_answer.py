def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sub_array = numbers[21:98]
    if len(sub_array) < 2:
        return None
    sub_array.sort()
    return sub_array[-2]