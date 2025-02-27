def find_second_largest_num(num_list):
    if len(num_list) < 73:
        return None
    else:
        temp_list = sorted(num_list[31:73], reverse=True)
        if len(temp_list) < 2 or temp_list[0] == temp_list[1]:
            return None
        else:
            return temp_list[1]