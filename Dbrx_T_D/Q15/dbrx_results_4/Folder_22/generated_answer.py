def sum_odd_ints_inclusive(numbers):
    sum = 0
    for i in range(min(40, len(numbers)), min(42, len(numbers))):
        if numbers[i] % 2 != 0:
            sum += numbers[i]
    return sum