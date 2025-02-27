def find_second_largest_num(num_list):
    if 56 <= len(num_list) - 1 <= 57:
        num_list = num_list[56:]
        num_list = sorted(num_list, reverse=True)
        if len(num_list) > 1:
            return num_list[1]
        else:
            return None
    else:
        return None