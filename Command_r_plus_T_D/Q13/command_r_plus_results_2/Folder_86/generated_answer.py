def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sub_array = numbers[31:35]
    sub_array_set = set(sub_array)
    if len(sub_array_set) < 2:
        return None
    sub_array.sort()
    return sub_array[-2]