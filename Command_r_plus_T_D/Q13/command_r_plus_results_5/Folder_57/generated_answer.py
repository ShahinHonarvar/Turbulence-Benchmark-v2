def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sub_list = numbers[27:56]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]