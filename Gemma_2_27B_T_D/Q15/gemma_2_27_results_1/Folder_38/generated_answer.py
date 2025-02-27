def sum_odd_ints_inclusive(numbers):
    sum = 0
    for i in range(22, 64):
        if i < len(numbers) and numbers[i] % 2 != 0:
            sum += numbers[i]
    return sum