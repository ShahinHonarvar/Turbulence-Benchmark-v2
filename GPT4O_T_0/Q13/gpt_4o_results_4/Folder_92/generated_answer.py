def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sub_list = numbers[0:2]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]