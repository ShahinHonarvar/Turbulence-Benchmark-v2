def sum_in_range(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        if 3 <= num <= 8:
            total += num
    return total