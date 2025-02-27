def sum_in_range(numbers: list[int]) -> int:
    total_sum = 0
    for num in numbers:
        if 39 <= num <= 43:
            total_sum += num
    return total_sum