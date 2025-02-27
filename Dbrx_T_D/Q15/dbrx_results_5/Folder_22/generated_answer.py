def sum_odd_ints_inclusive(int_list):
    sub_list = int_list[40:42]
    odd_numbers = [i for i in sub_list if i % 2 != 0]
    return sum(odd_numbers) if odd_numbers else 0