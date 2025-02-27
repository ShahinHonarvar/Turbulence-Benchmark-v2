def sum_odd_ints_inclusive(num_list):
    odd_nums = [n for n in num_list[70:85] if n % 2 != 0]
    return sum(odd_nums) if odd_nums else 0