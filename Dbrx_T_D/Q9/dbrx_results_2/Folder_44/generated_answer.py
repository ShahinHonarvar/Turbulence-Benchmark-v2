def all_odd_ints_inclusive(numbers):
    odd_ints = []
    if len(numbers) >= 69:
        for i in range(13, 69):
            if numbers[i] % 2 != 0:
                odd_ints.append(numbers[i])
    return odd_ints