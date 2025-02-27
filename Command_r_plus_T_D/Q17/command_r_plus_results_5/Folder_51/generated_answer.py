def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both_nums = []
    for num in numbers_list[6:10]:
        if num % -1 == 0 and num % -10 == 0:
            divisible_by_both_nums.append(num)
    return divisible_by_both_nums