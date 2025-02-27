def sum_even_ints_inclusive(numbers):
    sum = 0
    for i in range(len(numbers)):
        if i >= 70 and i <= 84:
            if numbers[i] % 2 == 0:
                sum += numbers[i]
    return sum