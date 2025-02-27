def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = []
    for num in numbers_list[69:98]:
        if num % -90 == 0 and num % -67 == 0:
            divisible_by_both.append(num)
    return divisible_by_both