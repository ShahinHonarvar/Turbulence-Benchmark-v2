def find_second_smallest_num(numbers):
    if len(numbers) <= 51:
        return None
    sub_list = sorted(numbers[29:52])
    if len(sub_list) < 2:
        return None
    return sub_list[1]