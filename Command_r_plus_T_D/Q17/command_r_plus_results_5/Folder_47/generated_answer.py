def all_ints_div_by_both_two_nums(lst: list[int]) -> list[int]:
    divisor_1, divisor_2 = (-90, -74)
    start_idx, end_idx = (42, 87)
    divisible_nums = [num for num in lst[start_idx:end_idx + 1] if num % divisor_1 == 0 and num % divisor_2 == 0]
    return divisible_nums