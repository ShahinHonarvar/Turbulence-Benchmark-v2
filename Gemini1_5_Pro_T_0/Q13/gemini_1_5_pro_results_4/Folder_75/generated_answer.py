def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    sub_list = numbers[56:58]
    if len(sub_list) == 1:
        return None
    sub_list.sort()
    return sub_list[0]