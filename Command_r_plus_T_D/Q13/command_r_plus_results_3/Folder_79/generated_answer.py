def find_second_largest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 5:
        return None
    else:
        numbers_list = numbers_list[4:]
        numbers_list.sort()
        return numbers_list[1] if len(numbers_list) > 1 else None