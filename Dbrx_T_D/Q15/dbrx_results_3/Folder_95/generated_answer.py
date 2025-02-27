def sum_odd_ints_inclusive(numbers):
    slice = numbers[82:87]
    result = 0
    for num in slice:
        if num % 2 != 0:
            result += num
    return result