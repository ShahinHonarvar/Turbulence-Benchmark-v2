def sum_odd_ints_inclusive(numbers):
    odd_sum = 0
    for i in range(13, 69):
        if i < len(numbers):
            if numbers[i] % 2 != 0:
                odd_sum += numbers[i]
    return odd_sum