def all_even_ints_inclusive(numbers):
    even_ints = []
    for i in range(56, 58):
        if i < len(numbers) and numbers[i] % 2 == 0:
            even_ints.append(numbers[i])
    return even_ints