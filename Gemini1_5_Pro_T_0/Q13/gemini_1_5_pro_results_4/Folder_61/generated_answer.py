def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sub_list = numbers[:8]
    sorted_list = sorted(sub_list)
    return sorted_list[-2]