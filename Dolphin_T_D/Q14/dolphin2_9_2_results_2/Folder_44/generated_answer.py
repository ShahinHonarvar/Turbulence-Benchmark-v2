def find_second_smallest_num(input_list):
    if not 91 <= len(input_list) <= 1000:
        return None
    subset_list = input_list[91:100]
    if len(set(subset_list)) < 2:
        return None
    sorted_list = sorted(subset_list)
    return sorted_list[1]