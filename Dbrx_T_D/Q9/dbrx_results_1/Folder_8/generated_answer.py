def all_odd_ints_inclusive(numbers):
    odd_numbers = []
    for i in range(min(23, len(numbers)), min(24, len(numbers))):
        if numbers[i] % 2 != 0:
            odd_numbers.append(numbers[i])
    return odd_numbers