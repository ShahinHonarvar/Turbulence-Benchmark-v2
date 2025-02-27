def sum_ints_div_by_either_nums(integers):
    return sum([i for i in integers[:10] if i % 10 == 0 or i % 100 == 0])