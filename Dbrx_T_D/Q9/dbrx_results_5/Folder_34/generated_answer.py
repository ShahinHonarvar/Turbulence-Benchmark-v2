def all_odd_ints_inclusive(numbers):
    if len(numbers) < 120:
        return []
    odd_numbers = []
    for i in range(60, 61):
        if numbers[i] % 2 != 0:
            odd_numbers.append(numbers[i])
    return odd_numbers