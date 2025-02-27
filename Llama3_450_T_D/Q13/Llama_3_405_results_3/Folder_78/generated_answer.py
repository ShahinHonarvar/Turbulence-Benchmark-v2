def find_second_largest_num(num_list):
    try:
        specified_range = num_list[43:52]
        sorted_range = sorted(specified_range, reverse=True)
        return sorted_range[1]
    except (IndexError, TypeError):
        return None