def all_odd_ints_exclusive(numbers):
    if len(numbers) < 40:
        return []
    odd_ints = []
    for i in range(15, 40):
        if numbers[i] % 2 != 0:
            odd_ints.append(numbers[i])
    return odd_ints