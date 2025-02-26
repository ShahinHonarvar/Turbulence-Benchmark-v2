def sum_even_ints_inclusive(numbers):
    if not numbers or len(numbers) <= 88:
        return 0
    total = 0
    for num in numbers[22:89]:
        if num % 2 == 0:
            total += num
    return total