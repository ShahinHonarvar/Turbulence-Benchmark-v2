def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 66:
        return 'Error: List too short'
    sum = 0
    for i in range(64, 67):
        if numbers[i] % 2 != 0:
            sum += numbers[i]
    return sum