def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 6:
        return None
    sub_list = numbers[1:6]
    if len(set(sub_list)) != len(sub_list):
        return None
    sub_list.sort()
    return sub_list[-2]