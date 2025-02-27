def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers or len(numbers) < 80:
        return None
    sub_list = numbers[29:80]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]