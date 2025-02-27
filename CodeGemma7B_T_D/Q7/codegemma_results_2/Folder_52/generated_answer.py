def all_even_ints_inclusive(numbers):
    result = []
    for i in range(28, 39):
        if numbers[i] % 2 == 0:
            result.append(numbers[i])
    return result