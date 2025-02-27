def sum_odd_ints_inclusive(numbers):
    sum_odd = 0
    for i in range(40, 42):
        if i >= 0 and i < len(numbers) and (numbers[i] % 2 != 0):
            sum_odd += numbers[i]
    return sum_odd