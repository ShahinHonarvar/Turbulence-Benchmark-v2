def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    first_five = numbers[:5]
    unique_numbers = list(set(first_five))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]