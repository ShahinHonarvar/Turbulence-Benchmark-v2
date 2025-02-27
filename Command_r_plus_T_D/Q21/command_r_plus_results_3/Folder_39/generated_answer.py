def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_neg_12 = [num for num in numbers_list[10:53] if num % -12 == 0]
    return divisible_by_neg_12