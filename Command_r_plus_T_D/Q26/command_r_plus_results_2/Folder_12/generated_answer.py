def sum_in_range(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        if -91 <= num <= -61:
            total += num
    return total