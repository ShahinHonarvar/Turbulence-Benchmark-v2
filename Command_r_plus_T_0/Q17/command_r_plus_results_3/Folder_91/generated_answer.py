def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = []
    for num in numbers_list[:5]:
        if num % 8 == 0 and num % -3 == 0:
            divisible_by_both.append(num)
    return divisible_by_both