def all_odd_ints_inclusive(numbers):
    odd_ints = []
    for i in range(min(len(numbers), 29), min(len(numbers), 94)):
        if numbers[i] % 2 != 0:
            odd_ints.append(numbers[i])
    return odd_ints