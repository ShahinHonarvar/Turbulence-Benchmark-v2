def find_second_largest_num(numbers):
    if len(numbers) < 51 or 22 >= len(numbers):
        return None
    sub_list = numbers[22:51]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]