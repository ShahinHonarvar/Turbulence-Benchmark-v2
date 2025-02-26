def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 32:
        return 0
    odd_sum = 0
    for num in numbers[28:33]:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum