def find_second_largest_num(num_list):
    subset = num_list[667:775]
    if len(subset) < 2:
        return None
    max_num = max(subset)
    subset.remove(max_num)
    if len(subset) == 1:
        return max(subset)
    second_max_num = max(subset)
    return second_max_num