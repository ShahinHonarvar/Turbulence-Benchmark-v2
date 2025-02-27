def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers or len(numbers) < 67:
        return None
    sub_list = numbers[10:67]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]