def sum_even_ints_inclusive(numbers):
    if len(numbers) < 2:
        return 0
    sum = 0
    for i in numbers[0:2]:
        if i % 2 == 0:
            sum += i
    return sum