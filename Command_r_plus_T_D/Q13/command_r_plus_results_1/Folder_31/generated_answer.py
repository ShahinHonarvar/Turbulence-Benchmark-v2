def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    if len(numbers) < 89 or len(numbers) < 76:
        return None
    sub_list = numbers[75:89]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]