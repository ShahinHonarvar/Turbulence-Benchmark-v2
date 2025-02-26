def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 200:
        return 0
    odd_sum = 0
    for index in range(70, 201):
        if numbers[index] % 2 != 0:
            odd_sum += numbers[index]
    return odd_sum