def find_second_largest_num(num_list):
    try:
        nums = sorted(num_list[20:31])
        return nums[-2]
    except IndexError:
        return None