def find_second_largest_num(list_numbers):
    if not list_numbers or len(list_numbers) < 2:
        return None
    sublist = list_numbers[55:99]
    max_num = max(sublist)
    sublist.remove(max_num)
    if not sublist:
        return None
    second_max_num = max(sublist)
    for num in sublist:
        if num != max_num and num != second_max_num:
            return num
    return None