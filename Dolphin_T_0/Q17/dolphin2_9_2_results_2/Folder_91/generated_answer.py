def all_ints_div_by_both_two_nums(integers: list) -> list:
    return [i for i in integers[:5] if i % 8 == 0 and i % -3 == 0]