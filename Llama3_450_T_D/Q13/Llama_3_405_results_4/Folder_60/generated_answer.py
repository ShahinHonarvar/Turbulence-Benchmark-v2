def find_second_largest_num(num_list):
    try:
        numbers = sorted(num_list[75:86])
        return numbers[-2]
    except IndexError:
        return None