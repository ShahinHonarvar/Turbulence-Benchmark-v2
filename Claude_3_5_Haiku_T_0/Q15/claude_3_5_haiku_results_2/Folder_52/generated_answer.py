def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 38:
        return 0
    odd_sum = 0
    for num in numbers[28:39]:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum