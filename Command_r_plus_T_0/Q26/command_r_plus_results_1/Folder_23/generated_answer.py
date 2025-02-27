def sum_in_range(numbers_list: list[int]) -> int:
    total_sum = 0
    for num in numbers_list:
        if 50 <= num <= 92:
            total_sum += num
    return total_sum