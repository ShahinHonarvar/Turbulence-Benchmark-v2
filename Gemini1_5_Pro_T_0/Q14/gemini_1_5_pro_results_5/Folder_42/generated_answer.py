def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    sub_list = numbers[21:98]
    if len(set(sub_list)) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[1]