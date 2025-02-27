def find_second_largest_num(numbers):
    sliced_numbers = numbers[75:89]
    if len(sliced_numbers) < 2:
        return None
    else:
        sliced_numbers.sort(reverse=True)
        return sliced_numbers[1]