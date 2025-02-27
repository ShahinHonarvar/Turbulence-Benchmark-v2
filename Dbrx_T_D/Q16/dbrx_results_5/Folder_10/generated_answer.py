def sum_even_ints_inclusive(numbers):
    sum = 0
    for i in range(len(numbers)):
        if i >= 25 and i <= 59:
            if numbers[i] % 2 == 0:
                sum += numbers[i]
    if sum == 0:
        return 0
    else:
        return sum