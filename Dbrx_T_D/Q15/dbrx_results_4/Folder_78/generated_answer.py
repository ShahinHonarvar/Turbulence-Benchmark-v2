def sum_odd_ints_inclusive(numbers):
    summed = 0
    for i in range(43, 52):
        if i >= len(numbers):
            break
        if numbers[i] % 2 != 0:
            summed += numbers[i]
    return summed