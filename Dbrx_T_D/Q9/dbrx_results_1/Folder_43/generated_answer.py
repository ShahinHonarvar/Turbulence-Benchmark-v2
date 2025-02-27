def all_odd_ints_inclusive(numbers):
    odd_ints = []
    for i in range(len(numbers)):
        if i >= 68 and i <= 86:
            if numbers[i] % 2 != 0:
                odd_ints.append(numbers[i])
    return odd_ints