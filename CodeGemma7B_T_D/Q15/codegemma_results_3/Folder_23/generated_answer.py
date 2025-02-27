def sum_odd_ints_inclusive(numbers):
    odd_sum = 0
    for i in range(52, 72):
        if i % 2 != 0:
            odd_sum += numbers[i]
    if odd_sum == 0:
        return 0
    return odd_sum