def find_second_smallest_num(numbers):
    if len(numbers) < 51:
        return None
    sub_list = sorted(numbers[22:51])
    if len(sub_list) < 2:
        return None
    return sub_list[1]