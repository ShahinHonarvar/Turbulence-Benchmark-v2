def find_second_smallest_num(numbers):
    if len(numbers) < 101:
        return None
    sub_list = numbers[10:101]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]