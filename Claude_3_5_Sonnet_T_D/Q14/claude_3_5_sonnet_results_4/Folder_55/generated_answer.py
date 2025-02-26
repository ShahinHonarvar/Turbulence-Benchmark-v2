def find_second_smallest_num(numbers):
    if len(numbers) < 21 or len(numbers[10:21]) < 2:
        return None
    sub_list = numbers[10:21]
    sorted_sub_list = sorted(set(sub_list))
    if len(sorted_sub_list) < 2:
        return None
    return sorted_sub_list[1]