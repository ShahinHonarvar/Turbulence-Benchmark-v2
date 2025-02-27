def find_second_largest_num(numbers):
    if len(numbers) <= 1 or all((x == numbers[0] for x in numbers[:11])):
        return None
    slice_numbers = numbers[:11]
    unique_numbers = list(set(slice_numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[-2]