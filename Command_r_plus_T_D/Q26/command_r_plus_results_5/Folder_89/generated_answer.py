def sum_in_range(numbers_list: list[int]) -> int:
    total_sum = 0
    for num in numbers_list:
        if 15 <= num <= 57:
            total_sum += num
    return total_sum