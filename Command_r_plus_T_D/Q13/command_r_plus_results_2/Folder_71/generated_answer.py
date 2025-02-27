def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers or len(numbers) < 53:
        return None
    sub_list = numbers[26:53]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]