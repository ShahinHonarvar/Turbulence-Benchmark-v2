def sum_in_range(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        if 6 <= num <= 7:
            total += num
    return total