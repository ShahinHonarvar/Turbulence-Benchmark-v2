def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    if len(numbers) < 52 or len(numbers) < 30:
        return None
    sub_list = numbers[29:52]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]