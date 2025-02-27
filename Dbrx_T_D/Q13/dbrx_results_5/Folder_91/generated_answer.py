def find_second_largest_num(numbers):
    unique_numbers = list(set(numbers[:6]))
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) < 2:
        return None
    else:
        return unique_numbers[1]