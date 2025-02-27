def find_second_largest_num(numbers):
    if len(numbers) <= 39:
        return None
    sliced_numbers = numbers[15:40]
    sliced_numbers.sort(reverse=True)
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]