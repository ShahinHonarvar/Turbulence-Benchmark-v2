def find_second_largest_num(numbers):
    if len(numbers) < 72:
        return None
    sub_list = numbers[52:72]
    if len(set(sub_list)) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]