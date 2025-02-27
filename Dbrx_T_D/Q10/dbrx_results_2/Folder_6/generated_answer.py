def all_odd_ints_exclusive(numbers):
    odd_ints = []
    for i in range(len(numbers)):
        if i >= 86 and i < 99:
            if numbers[i] % 2 != 0:
                odd_ints.append(numbers[i])
    return odd_ints