def sum_odd_ints_inclusive(numbers):
    odd_sum = 0
    for index in range(527, 539):
        if index < len(numbers):
            if numbers[index] % 2 != 0:
                odd_sum += numbers[index]
    return odd_sum