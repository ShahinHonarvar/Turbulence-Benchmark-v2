def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 9:
        return None
    sorted_nums = sorted(num_list[1:9])
    return sorted_nums[1] if len(sorted_nums) >= 2 else None