def sum_odd_ints_inclusive(num_list):
    odd_nums = num_list[29:52]
    odd_nums = [x for x in odd_nums if x % 2 != 0]
    return sum(odd_nums) if len(odd_nums) > 0 else 0