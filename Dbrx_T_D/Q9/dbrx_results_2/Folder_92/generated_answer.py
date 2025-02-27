def all_odd_ints_inclusive(numbers):
    odd_ints = []
    for i in range(min(1, len(numbers)), max(1, len(numbers))):
        if numbers[i] % 2 != 0:
            odd_ints.append(numbers[i])
    return odd_ints