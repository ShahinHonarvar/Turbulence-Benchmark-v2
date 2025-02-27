def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    sub_list = numbers[:9]
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]