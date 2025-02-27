def sum_in_range(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        if 18 <= num <= 52:
            total += num
    return total