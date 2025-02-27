def sum_even_ints_inclusive(numbers):
    if len(numbers) < 2:
        return 0
    start, end = (numbers[0], numbers[1])
    return sum((x for x in range(start, end + 1) if x % 2 == 0))