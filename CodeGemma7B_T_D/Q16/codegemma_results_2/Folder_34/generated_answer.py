def sum_even_ints_inclusive(numbers):
    total_sum = 0
    for i in range(60, 201):
        if i % 2 == 0:
            total_sum += numbers[i]
    if total_sum > 0:
        return total_sum
    else:
        return 0