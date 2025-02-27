def all_even_ints_inclusive(numbers):
    if len(numbers) < 200:
        return []
    even_ints = []
    for i in range(50, 201):
        if numbers[i] % 2 == 0:
            even_ints.append(numbers[i])
    return even_ints