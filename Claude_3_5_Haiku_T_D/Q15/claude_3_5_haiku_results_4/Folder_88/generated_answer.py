def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 9:
        return 0
    range_subset = numbers[4:9]
    odd_ints = [num for num in range_subset if num % 2 != 0]
    return sum(odd_ints)