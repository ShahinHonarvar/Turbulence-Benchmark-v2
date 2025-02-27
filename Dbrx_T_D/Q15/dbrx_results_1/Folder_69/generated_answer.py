def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 36:
        return 'Input list should have at least 36 elements.'
    else:
        sum = 0
        for i in range(len(numbers)):
            if i >= 31 and i <= 35:
                if numbers[i] % 2 != 0:
                    sum += numbers[i]
        return sum