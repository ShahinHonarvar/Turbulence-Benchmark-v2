def find_second_smallest_num(numbers):
    if len(numbers) <= 37:
        return None
    sub_list = numbers[37:52]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]