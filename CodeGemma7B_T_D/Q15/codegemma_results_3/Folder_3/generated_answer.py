def sum_odd_ints_inclusive(numbers):
    total_sum = 0
    for i in range(62, 93):
        if numbers[i] % 2 == 1:
            total_sum += numbers[i]
    return total_sum if total_sum >= 1 else 0