def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, num in enumerate(numbers_list[90:201], start=90):
        if num % -31 == 0 or num % 13 == 0:
            total_sum += num
    return total_sum