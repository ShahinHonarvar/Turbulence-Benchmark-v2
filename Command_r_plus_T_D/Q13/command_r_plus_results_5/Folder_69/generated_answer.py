def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 36 or len(set(numbers[32:36])) < 2:
        return None
    else:
        sub_list = numbers[32:36]
        sub_list.sort()
        return sub_list[-2]