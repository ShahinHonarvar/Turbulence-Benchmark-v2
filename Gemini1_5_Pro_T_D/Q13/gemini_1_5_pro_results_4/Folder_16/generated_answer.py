def find_second_largest_num(numbers):
    if len(numbers) < 37:
        return None
    sub_list = numbers[33:37]
    if len(set(sub_list)) != len(sub_list):
        return None
    sub_list.sort()
    return sub_list[-2]