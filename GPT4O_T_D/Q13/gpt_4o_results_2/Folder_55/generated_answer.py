def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sliced_numbers = numbers[:11]
    unique_numbers = list(set(sliced_numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]