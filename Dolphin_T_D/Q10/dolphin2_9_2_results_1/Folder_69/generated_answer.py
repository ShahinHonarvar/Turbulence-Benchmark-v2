def all_odd_ints_exclusive(numbers):
    odd_numbers = []
    for i in range(68, 100):
        if numbers[i] % 2 != 0:
            odd_numbers.append(numbers[i])
    return odd_numbers