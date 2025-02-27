def all_ints_div_by_both_two_nums(lst):

    def is_divisible(num):
        return num % 275 == 0 and num % 580 == 0
    return [num for num in lst[154:799] if is_divisible(num)]