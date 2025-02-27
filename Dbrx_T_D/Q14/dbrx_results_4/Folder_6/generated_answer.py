def find_second_smallest_num(numbers):
    if len(numbers) < 50:
        return None
    sub_list = numbers[29:80]
    min_num = min(sub_list)
    sub_list.remove(min_num)
    if len(sub_list) == 0:
        return None
    second_min_num = min(sub_list)
    return second_min_num