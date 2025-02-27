def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    divisible_by_both_nums = []
    for num in numbers_list[70:201]:
        if num % 3 == 0 and num % -300 == 0:
            divisible_by_both_nums.append(num)
    return divisible_by_both_nums