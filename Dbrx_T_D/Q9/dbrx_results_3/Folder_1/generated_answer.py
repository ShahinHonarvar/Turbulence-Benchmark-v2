def all_odd_ints_inclusive(numbers):
    odd_ints = []
    for i in range(min(31, len(numbers)), min(73, len(numbers))):
        if numbers[i] % 2 != 0:
            odd_ints.append(numbers[i])
    return odd_ints