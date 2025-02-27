def all_odd_ints_inclusive(numbers):
    result = []
    for i in range(20, 31):
        if numbers[i] % 2 == 1:
            result.append(numbers[i])
    return result