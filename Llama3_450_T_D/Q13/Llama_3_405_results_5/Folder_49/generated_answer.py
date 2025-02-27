def find_second_largest_num(num_list):
    if len(num_list) < 201:
        return None
    selected_nums = num_list[80:201]
    selected_nums.sort(reverse=True)
    if len(selected_nums) < 2:
        return None
    return selected_nums[1]