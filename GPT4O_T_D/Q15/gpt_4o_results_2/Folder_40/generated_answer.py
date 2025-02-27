def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 3:
        range_to_check = numbers
    else:
        range_to_check = numbers[:3]
    return sum((num for num in range_to_check if num % 2 != 0))