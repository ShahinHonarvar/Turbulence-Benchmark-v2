def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers or len(numbers) < 10:
        return None
    else:
        sub_list = numbers[8:10]
        sub_list.sort()
        return sub_list[1] if len(sub_list) == 2 else None