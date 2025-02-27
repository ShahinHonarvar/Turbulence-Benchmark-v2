def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    if len(numbers) < 371:
        return None
    sub_array = numbers[310:371]
    sub_array.sort()
    if len(sub_array) < 2:
        return None
    return sub_array[-2]