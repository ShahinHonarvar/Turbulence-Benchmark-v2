def find_second_largest_num(num_list):
    if len(num_list[200:30:-1]) < 2:
        return None
    else:
        second_largest = sorted(num_list[200:30:-1], reverse=True)[1]
        return second_largest