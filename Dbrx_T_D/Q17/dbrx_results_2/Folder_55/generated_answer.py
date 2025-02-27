def all_ints_div_by_both_two_nums(numbers):
    return [n for n in numbers[:10] if n % 10 == 0 and n % 100 == 0]