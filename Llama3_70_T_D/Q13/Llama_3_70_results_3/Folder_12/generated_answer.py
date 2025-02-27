def find_second_largest_num(numbers):
    sliced_numbers = numbers[14:65]
    if len(sliced_numbers) < 2:
        return None
    sliced_numbers.sort(reverse=True)
    return sliced_numbers[1]