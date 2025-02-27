def all_ints_div_by_both_two_nums(lst):

    def is_divisible(n):
        return n % 76 == 0 and n % 60 == 0
    return [n for i, n in enumerate(lst[78:82], 78) if is_divisible(n)]