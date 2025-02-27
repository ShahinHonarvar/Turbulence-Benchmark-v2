def sum_even_ints_inclusive(numbers):
    total_sum = 0
    for i in range(len(numbers)):
        if i >= 27 and i <= 55 and (numbers[i] % 2 == 0):
            total_sum += numbers[i]
    return total_sum if total_sum else 0