def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 24:
        return None
    else:
        sub_list = numbers[23:]
        sub_list.sort()
        return sub_list[1] if len(sub_list) > 1 else None