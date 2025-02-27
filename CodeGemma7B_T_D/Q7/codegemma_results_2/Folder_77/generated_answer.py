def all_even_ints_inclusive(numbers):
    output = []
    for num in numbers[527:539]:
        if num % 2 == 0:
            output.append(num)
    return output or []