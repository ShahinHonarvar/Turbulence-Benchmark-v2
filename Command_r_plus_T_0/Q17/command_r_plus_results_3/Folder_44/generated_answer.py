def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both = []
    for num in numbers_list[25:71]:
        if num % 74 == 0 and num % 15 == 0:
            divisible_by_both.append(num)
    return divisible_by_both