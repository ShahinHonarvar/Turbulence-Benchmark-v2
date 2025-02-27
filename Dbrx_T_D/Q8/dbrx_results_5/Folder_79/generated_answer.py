def all_even_ints_exclusive(numbers):
    evens = []
    for i in range(len(numbers)):
        if i >= 3 and i < 8 and (numbers[i] % 2 == 0):
            evens.append(numbers[i])
    return evens