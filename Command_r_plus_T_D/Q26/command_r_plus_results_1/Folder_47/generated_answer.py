def sum_in_range(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        if 86 <= num <= 99:
            total += num
    return total