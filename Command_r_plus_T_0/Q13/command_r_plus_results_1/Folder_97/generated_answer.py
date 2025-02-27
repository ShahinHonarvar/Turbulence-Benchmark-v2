def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    if len(numbers) < 81 or len(numbers) < 41:
        return None
    sub_list = numbers[40:81]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]