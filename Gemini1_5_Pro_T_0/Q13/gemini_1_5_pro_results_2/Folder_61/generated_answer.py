def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sub_list = numbers[:8]
    if len(set(sub_list)) != len(sub_list):
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[-2]