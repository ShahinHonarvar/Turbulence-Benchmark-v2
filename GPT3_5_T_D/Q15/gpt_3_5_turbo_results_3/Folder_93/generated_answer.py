def sum_odd_ints_inclusive(lst):
    odd_nums = [num for num in lst[75:95] if num % 2 != 0]
    return sum(odd_nums) if odd_nums else 0