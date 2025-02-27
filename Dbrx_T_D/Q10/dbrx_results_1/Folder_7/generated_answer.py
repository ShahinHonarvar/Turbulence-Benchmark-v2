def all_odd_ints_exclusive(numbers):
    odd_numbers = []
    for i in range(323, 972):
        if i < len(numbers) and numbers[i] % 2 != 0:
            odd_numbers.append(numbers[i])
    return odd_numbers