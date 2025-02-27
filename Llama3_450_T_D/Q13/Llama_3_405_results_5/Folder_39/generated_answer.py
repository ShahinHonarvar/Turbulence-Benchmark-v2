def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    sliced_numbers = numbers[20:31]
    sliced_numbers.sort(reverse=True)
    if len(sliced_numbers) > 1:
        return sliced_numbers[1]
    return None