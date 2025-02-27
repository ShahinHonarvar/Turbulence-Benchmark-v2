def all_odd_ints_inclusive(numbers):
    odd_ints = []
    for i in range(10, 101):
        if i % 2 != 0 and i >= 10 and (i <= 100):
            odd_ints.append(numbers[i - 1])
    return odd_ints