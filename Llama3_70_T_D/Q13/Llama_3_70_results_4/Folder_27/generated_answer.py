def find_second_largest_num(num_list):
    try:
        temp_list = num_list[66:94]
        temp_list.sort(reverse=True)
        if len(temp_list) < 2:
            return None
        else:
            return temp_list[1]
    except IndexError:
        return None