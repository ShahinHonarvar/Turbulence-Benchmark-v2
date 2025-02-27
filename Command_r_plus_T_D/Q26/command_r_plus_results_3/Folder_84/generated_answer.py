def sum_in_range(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        if 113 <= num <= 392:
            total += num
    return total