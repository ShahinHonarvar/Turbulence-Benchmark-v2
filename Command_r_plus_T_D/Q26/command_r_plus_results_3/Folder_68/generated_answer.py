def sum_in_range(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        if 7 <= num <= 9:
            total += num
    return total