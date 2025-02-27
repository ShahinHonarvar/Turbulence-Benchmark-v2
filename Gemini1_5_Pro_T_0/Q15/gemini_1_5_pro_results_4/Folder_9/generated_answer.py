def sum_odd_ints_inclusive(numbers):
    sum = 0
    for i in range(max(0, min(70, len(numbers))), min(201, len(numbers))):
        if numbers[i] % 2 != 0:
            sum += numbers[i]
    return sum