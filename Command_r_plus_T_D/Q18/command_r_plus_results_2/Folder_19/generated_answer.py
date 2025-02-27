def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_numbers = 0
    for num in numbers_list[1:5]:
        if num % 4 == 0 or num % -6 == 0:
            sum_divisible_numbers += num
    return sum_divisible_numbers