def find_second_largest_num(num_list):
    if len(num_list) < 51:
        return None
    else:
        temp = sorted(num_list[22:51], reverse=True)
        if len(temp) < 2:
            return None
        else:
            return temp[1]