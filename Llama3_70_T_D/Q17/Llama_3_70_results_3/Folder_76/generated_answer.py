def all_ints_div_by_both_two_nums(lst):

    def is_divisible(n):
        return n % 850 == 0 and n % 587 == 0
    return [i for i in lst[250:630] if is_divisible(i)]