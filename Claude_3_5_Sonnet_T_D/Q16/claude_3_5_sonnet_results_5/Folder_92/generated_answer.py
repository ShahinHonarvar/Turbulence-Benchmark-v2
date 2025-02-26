def sum_even_ints_inclusive(numbers):
    if len(numbers) < 2:
        return 0
    start = numbers[0]
    end = numbers[1]
    if start > end:
        start, end = (end, start)
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    return total