def all_even_ints_inclusive(numbers):
    result = []
    for num in numbers[10:67]:
        if num % 2 == 0:
            result.append(num)
    return result