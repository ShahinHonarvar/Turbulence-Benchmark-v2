def sum_even_ints_inclusive(numbers):
    sum_even = 0
    for i in range(4, 5):
        if numbers[i] % 2 == 0:
            sum_even += numbers[i]
    return sum_even