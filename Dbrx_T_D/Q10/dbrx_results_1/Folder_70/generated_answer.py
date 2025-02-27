def all_odd_ints_exclusive(numbers):
    odd_ints = []
    for i in range(38, 81):
        if i >= len(numbers) or not isinstance(numbers[i], int):
            continue
        if numbers[i] % 2 != 0:
            odd_ints.append(numbers[i])
    return odd_ints