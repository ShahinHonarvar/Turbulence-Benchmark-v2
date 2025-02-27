def all_ints_div_by_num(integer_list):
    slice_of_list = integer_list[17:64]
    divisible_numbers = [number for number in slice_of_list if number % 89 == 0]
    return divisible_numbers