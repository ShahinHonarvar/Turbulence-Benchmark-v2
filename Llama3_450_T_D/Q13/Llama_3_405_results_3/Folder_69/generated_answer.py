def find_second_largest_num(numbers):
    sliced_numbers = numbers[32:36]
    sliced_numbers.sort(reverse=True)
    if len(sliced_numbers) < 2:
        return None
    else:
        return sliced_numbers[1]