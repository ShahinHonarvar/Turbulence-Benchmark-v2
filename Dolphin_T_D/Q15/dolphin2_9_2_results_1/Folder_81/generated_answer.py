def sum_odd_ints_inclusive(numbers):
    if len(numbers) == 0:
        return 0
    sum_odd = 0
    for i in range(10, len(numbers)):
        if numbers[i] % 2 != 0:
            sum_odd += numbers[i]
        if i > 100:
            break
    return sum_odd