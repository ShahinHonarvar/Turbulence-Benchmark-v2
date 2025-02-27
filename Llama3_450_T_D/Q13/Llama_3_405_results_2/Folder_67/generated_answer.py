def find_second_largest_num(numbers):
    if len(numbers) < 51 or 22 >= len(numbers):
        return None
    sliced_numbers = numbers[22:51]
    sliced_numbers.sort(reverse=True)
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]