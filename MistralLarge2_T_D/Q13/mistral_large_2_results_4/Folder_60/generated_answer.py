def find_second_largest_num(numbers):
    if len(numbers) < 86:
        return None
    sub_list = numbers[75:86]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]