def find_second_smallest_num(list_numbers):
    if len(list_numbers) < 2:
        return None
    sub_list = list_numbers[17:79]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]