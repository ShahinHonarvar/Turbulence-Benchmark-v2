def find_second_smallest_num(num_list):
    if 28 <= len(num_list) <= 40:
        sorted_list = sorted(num_list[28:41])
        return sorted_list[1] if len(sorted_list) > 1 else None