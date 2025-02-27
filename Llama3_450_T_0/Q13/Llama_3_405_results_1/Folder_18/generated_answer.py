def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return None
    sliced_numbers = numbers[35:50]
    if len(sliced_numbers) < 2:
        return None
    sliced_numbers.sort(reverse=True)
    return sliced_numbers[1]