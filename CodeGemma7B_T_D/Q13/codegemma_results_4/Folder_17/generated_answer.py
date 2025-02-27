def find_second_largest_num(num_list):
    num_list = sorted(num_list)
    if not num_list:
        return None
    try:
        second_largest = num_list[61:79][-2]
        return second_largest
    except IndexError:
        return None