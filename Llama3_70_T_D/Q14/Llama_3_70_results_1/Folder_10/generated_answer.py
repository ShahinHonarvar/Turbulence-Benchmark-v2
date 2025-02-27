def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    sub_list = sorted(numbers[62:93])
    if len(sub_list) < 2:
        return None
    return sub_list[1]