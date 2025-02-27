def sum_even_ints_inclusive(numbers):
    if not numbers:
        return 0
    start, end = (0, 0)
    while start < len(numbers) and numbers[start] % 2 != 0:
        start += 1
    if start == len(numbers):
        return 0
    end = start
    while end < len(numbers) and numbers[end] % 2 == 0:
        end += 1
    return sum(numbers[start:end + 1])