def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 58:
        return None
    else:
        sub_list = numbers[56:58]
        sub_list.sort()
        return sub_list[1]