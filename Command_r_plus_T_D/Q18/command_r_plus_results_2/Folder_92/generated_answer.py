def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for num in numbers_list[0:1]:
        if num % 1 == 0 or num % -1 == 0:
            total_sum += num
    return total_sum