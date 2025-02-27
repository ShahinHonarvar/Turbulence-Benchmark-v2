def find_second_smallest_num(numbers):
    if len(numbers) < 79:
        return None
    sub_list = sorted(numbers[17:79])
    if len(sub_list) < 2:
        return None
    return sub_list[1]