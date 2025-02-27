def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    sub_list = numbers[10:11]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[0]