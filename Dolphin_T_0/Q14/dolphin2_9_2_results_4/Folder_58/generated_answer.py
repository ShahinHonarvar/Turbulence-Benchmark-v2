def find_second_smallest_num(num_list):
    try:
        sublist = num_list[310:371]
        min_num = min(sublist)
        second_min_num = min((val for val in sublist if val != min_num))
        return second_min_num
    except ValueError:
        return None