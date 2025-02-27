def sum_odd_ints_inclusive(int_list):
    odd_ints = [num for num in int_list[14:65] if num % 2 != 0]
    return sum(odd_ints) if odd_ints else 0