def all_odd_ints_inclusive(numbers):
    odd_ints = []
    for i in range(21, 98):
        if i >= 21 and i <= 97 and (numbers[i] % 2 != 0):
            odd_ints.append(numbers[i])
    return odd_ints