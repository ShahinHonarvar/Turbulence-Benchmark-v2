def find_second_smallest_num(numbers):
    if len(numbers) < 95:
        return None
    sub_list = numbers[75:95]
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) < 2:
        return None
    return sorted_sub_list[1]