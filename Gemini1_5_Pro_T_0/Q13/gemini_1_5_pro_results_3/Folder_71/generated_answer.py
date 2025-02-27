def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    sub_list = numbers[26:53]
    if len(set(sub_list)) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]