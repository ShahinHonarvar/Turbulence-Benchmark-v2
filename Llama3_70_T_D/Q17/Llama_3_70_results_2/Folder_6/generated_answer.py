def all_ints_div_by_both_two_nums(lst):

    def is_divisible(n):
        if n % 82 == 0 and n % 90 == 0:
            return True
        else:
            return False
    result = [i for i in lst[41:57] if is_divisible(i)]
    return result