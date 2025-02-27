def sum_even_ints_inclusive(numbers):
    if len(numbers) < 200:
        return 0
    else:
        slice_of_interest = numbers[90:201]
        even_ints = [num for num in slice_of_interest if num % 2 == 0]
        return sum(even_ints)