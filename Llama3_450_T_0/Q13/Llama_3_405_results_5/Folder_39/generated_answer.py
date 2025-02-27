def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    sliced_numbers = numbers[20:31]
    if len(sliced_numbers) < 2:
        return None
    sliced_numbers.sort(reverse=True)
    return sliced_numbers[1]