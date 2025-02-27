def all_odd_ints_exclusive(numbers):
    start = 369
    end = 983
    odd_ints = []
    if len(numbers) < end:
        return odd_ints
    for i in range(start, end):
        if numbers[i] % 2 != 0:
            odd_ints.append(numbers[i])
    return odd_ints