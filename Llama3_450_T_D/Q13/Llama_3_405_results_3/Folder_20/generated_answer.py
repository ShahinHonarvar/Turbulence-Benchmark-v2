def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    sliced_numbers = numbers[56:67]
    sliced_numbers.sort(reverse=True)
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]