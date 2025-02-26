def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 72:
        return 0
    total = 0
    for num in numbers[31:73]:
        if num % 2 == 0:
            total += num
    return total