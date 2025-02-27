def find_second_largest_num(num_list):
    if len(num_list) < 201 or max(num_list) < num_list[80]:
        return None
    num_list = sorted(num_list[80:201], reverse=True)
    return num_list[1]