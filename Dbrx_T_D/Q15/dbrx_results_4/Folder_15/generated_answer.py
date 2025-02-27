def sum_odd_ints_inclusive(numbers):
    sum = 0
    for i in range(min(3, len(numbers))):
        if numbers[i] % 2 != 0:
            sum += numbers[i]
    if len(numbers) > 3 and numbers[3] % 2 != 0:
        sum += numbers[3]
    return sum if sum > 0 else 0