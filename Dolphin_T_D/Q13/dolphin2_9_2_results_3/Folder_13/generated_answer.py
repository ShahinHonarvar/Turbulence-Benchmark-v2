def find_second_largest_num(input_list):
    if 25 <= 87 < len(input_list):
        subset_list = input_list[25:88]
        if not set(subset_list):
            return None
        else:
            sorted_list = sorted(set(subset_list), reverse=True)
            if len(sorted_list) > 1:
                return sorted_list[1]
            else:
                return None
    else:
        return None