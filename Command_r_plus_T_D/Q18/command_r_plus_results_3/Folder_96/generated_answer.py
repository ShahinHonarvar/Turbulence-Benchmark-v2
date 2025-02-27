def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for index, num in enumerate(numbers_list[50:201], start=50):
        if num % -34 == 0 or num % 64 == 0:
            sum_divisible += num
    return sum_divisible