def sum_even_ints_inclusive(numbers):
    sum = 0
    for i in range(len(numbers)):
        if i < 0 or i > 10:
            break
        if numbers[i] % 2 == 0:
            sum += numbers[i]
    return sum