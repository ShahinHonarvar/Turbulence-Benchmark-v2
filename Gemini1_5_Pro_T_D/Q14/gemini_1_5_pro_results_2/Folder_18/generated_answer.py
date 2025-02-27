def find_second_smallest_num(numbers):
    if len(numbers) < 49:
        return None
    sub_list = numbers[30:49]
    if len(set(sub_list)) != len(sub_list):
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]