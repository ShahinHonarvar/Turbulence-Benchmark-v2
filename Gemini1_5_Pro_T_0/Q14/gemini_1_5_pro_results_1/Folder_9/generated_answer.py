def find_second_smallest_num(numbers):
    if len(numbers) < 71 or len(numbers) > 201:
        return None
    sub_list = numbers[70:201]
    if len(set(sub_list)) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]