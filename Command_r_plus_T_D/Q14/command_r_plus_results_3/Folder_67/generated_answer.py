def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 55:
        return None
    sub_list = sorted(numbers[50:55])
    if len(sub_list) < 2:
        return None
    return sub_list[1]