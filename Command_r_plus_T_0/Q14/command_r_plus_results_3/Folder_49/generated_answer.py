def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sub_list = sorted(numbers[80:201])
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]