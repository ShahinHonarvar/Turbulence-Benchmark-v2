def all_odd_ints_inclusive(numbers):
    odd_ints = []
    for i in range(1, 6):
        if i < len(numbers) and numbers[i] % 2 != 0:
            odd_ints.append(numbers[i])
    return odd_ints