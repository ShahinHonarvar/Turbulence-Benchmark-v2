def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 82:
        return 'Input list too small, cannot access index 82'
    sum = 0
    for i in range(56, 83):
        if numbers[i] % 2 != 0:
            sum += numbers[i]
    return sum