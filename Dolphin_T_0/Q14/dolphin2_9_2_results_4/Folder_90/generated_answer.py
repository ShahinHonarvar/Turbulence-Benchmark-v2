def find_second_smallest_num(num_list):
    if len(num_list) < 2 or (len(set(num_list)) == 1 and len(num_list) > 0):
        return None
    sliced_list = num_list[527:538 + 1]
    sorted_list = sorted(set(sliced_list))
    return sorted_list[1] if len(sorted_list) > 1 else None