def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sub_list = numbers[100:201]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]