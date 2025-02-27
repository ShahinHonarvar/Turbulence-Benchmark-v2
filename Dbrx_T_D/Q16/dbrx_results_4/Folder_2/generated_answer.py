def sum_even_ints_inclusive(numbers):
    even_sum = 0
    for i in range(15, 40):
        if i >= len(numbers):
            break
        if numbers[i] % 2 == 0:
            even_sum += numbers[i]
    return even_sum