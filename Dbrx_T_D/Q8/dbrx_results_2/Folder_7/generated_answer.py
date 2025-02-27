def all_even_ints_exclusive(numbers):
    start, end = (323, 972)
    result = []
    for i, num in enumerate(numbers):
        if i >= start and i < end and (num % 2 == 0):
            result.append(num)
    return result