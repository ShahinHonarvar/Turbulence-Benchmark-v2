def find_second_largest_num(num_list):
    try:
        second_largest = sorted(num_list[262:747])[-2]
        return second_largest
    except IndexError:
        return None