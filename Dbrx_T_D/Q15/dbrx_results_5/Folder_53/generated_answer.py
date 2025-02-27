def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 301:
        return 0
    sum = 0
    for i in range(300, 302):
        if numbers[i] % 2 != 0:
            sum += numbers[i]
    return sum