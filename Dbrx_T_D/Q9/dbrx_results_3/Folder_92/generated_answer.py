def all_odd_ints_inclusive(numbers):
    odd_numbers = []
    for i in range(numbers[0], numbers[1] + 1):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers