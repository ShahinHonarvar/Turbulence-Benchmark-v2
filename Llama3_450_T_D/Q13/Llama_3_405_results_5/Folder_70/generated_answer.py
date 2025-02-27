def find_second_largest_num(numbers):
    if len(numbers) < 2 or 32 > len(numbers) - 1:
        return None
    sliced_numbers = numbers[28:33]
    sliced_numbers.sort(reverse=True)
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]