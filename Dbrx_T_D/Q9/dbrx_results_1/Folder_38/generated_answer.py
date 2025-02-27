def all_odd_ints_inclusive(numbers):
    if len(numbers) < 63:
        return []
    odd_ints = []
    for i in range(22, 64):
        if numbers[i] % 2 != 0:
            odd_ints.append(numbers[i])
    return odd_ints