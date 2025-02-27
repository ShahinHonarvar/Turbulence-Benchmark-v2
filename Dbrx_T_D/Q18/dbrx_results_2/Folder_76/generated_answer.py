def sum_ints_div_by_either_nums(numbers):
    target_multiple_850 = [x for x in numbers[250:630] if x % 850 == 0]
    target_multiple_587 = [x for x in numbers[250:630] if x % 587 == 0]
    return sum(target_multiple_850 + target_multiple_587)