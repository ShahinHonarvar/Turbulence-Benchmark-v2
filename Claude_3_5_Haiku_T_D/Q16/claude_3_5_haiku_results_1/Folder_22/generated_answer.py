def sum_even_ints_inclusive(numbers):
    if len(numbers) < 42:
        return 0
    sum_even = 0
    for num in numbers[40:42]:
        if num % 2 == 0:
            sum_even += num
    return sum_even