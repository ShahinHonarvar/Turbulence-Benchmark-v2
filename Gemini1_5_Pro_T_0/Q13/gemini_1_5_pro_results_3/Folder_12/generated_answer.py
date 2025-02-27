def find_second_largest_num(numbers):
    if len(numbers) < 65:
        return None
    sub_list = numbers[14:65]
    if len(set(sub_list)) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]