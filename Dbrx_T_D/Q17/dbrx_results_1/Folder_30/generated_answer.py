def all_ints_div_by_both_two_nums(int_list):
    target_divisors = (-81, -94)
    eligible_divisors = [divisor for divisor in target_divisors if divisor != 1]
    result = [num for num in int_list[11:77] if all((num % div == 0 for div in eligible_divisors))]
    return result