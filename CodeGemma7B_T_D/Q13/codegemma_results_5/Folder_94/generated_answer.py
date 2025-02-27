def find_second_largest_num(num_list):
    if num_list[28:41] == sorted(num_list[28:41], reverse=True)[1:]:
        return sorted(num_list[28:41], reverse=True)[1]
    else:
        return None