def all_even_ints_inclusive(numbers):
    result = []
    for i in range(75, 89):
        if i in numbers and i % 2 == 0:
            result.append(i)
    return result