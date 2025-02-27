def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers or len(numbers) < 6:
        return None
    sub_list = numbers[6:7]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]