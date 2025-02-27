def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 311:
        return None
    sublist = numbers[310:371]
    unique_numbers = list(set(sublist))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]