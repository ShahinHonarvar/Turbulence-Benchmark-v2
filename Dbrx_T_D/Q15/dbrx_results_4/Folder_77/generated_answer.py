def sum_odd_ints_inclusive(numbers):
    return sum(numbers[527:539]) if any(numbers[527:539] % 2 != 0) else 0