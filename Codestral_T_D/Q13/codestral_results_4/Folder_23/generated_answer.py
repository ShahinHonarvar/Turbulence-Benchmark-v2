def find_second_largest_num(num_list):
    if 52 <= len(num_list) <= 71:
        subset = sorted(num_list[52:72], reverse=True)
        return subset[1] if len(subset) > 1 else None
    return None