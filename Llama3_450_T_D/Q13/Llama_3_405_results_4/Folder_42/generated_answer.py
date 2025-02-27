def find_second_largest_num(num_list):
    try:
        distinct_nums = sorted(set(num_list[29:80]))
        if len(distinct_nums) < 2:
            return None
        return distinct_nums[-2]
    except IndexError:
        return None