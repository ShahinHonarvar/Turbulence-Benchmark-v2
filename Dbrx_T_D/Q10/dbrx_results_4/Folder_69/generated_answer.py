def all_odd_ints_exclusive(numbers):
    odd_ints = []
    if len(numbers) >= 100:
        for i in range(68, 99):
            if numbers[i] % 2 != 0:
                odd_ints.append(numbers[i])
    return odd_ints