def find_second_largest_num(num_list):
    num_list.sort()
    if len(num_list) <= 1 or num_list[len(num_list) - 1] == num_list[len(num_list) - 2]:
        return None
    else:
        return num_list[len(num_list) - 2]