def all_even_ints_inclusive(numbers):
    start, end = (0, 1)
    even_ints = []
    for i in range(start, end + 1):
        if i < len(numbers) and numbers[i] % 2 == 0:
            even_ints.append(numbers[i])
    return even_ints