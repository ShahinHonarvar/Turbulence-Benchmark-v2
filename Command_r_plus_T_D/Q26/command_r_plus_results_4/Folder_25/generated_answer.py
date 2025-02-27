def sum_in_range(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        if -10 <= num <= 48:
            total += num
    return total