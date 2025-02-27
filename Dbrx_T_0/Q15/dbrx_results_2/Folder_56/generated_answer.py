def sum_odd_ints_inclusive(numbers):
    if not numbers:
        return 0
    sum = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            sum += numbers[i]
        if i > 0 and numbers[i - 1] % 2 != 0:
            break
    return sum