def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 87:
        return 0
    odd_sum = 0
    for num in numbers[82:87]:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum