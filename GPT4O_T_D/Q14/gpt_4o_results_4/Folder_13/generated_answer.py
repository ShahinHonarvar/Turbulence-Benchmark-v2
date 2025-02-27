def find_second_smallest_num(numbers):
    if len(numbers) < 33:
        return None
    sub_list = numbers[28:33]
    sub_list_sorted = sorted(sub_list)
    if len(sub_list_sorted) < 2:
        return None
    return sub_list_sorted[1]