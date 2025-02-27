def sum_even_ints_inclusive(numbers):
    sum_even_ints = 0
    for i in range(26, 53):
        if i != len(numbers):
            if numbers[i] % 2 == 0:
                sum_even_ints += numbers[i]
    return sum_even_ints