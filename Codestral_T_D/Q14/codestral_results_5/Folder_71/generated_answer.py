def find_second_smallest_num(numbers):
    sliced_numbers = numbers[29:52]
    if len(sliced_numbers) < 2:
        return None
    else:
        sliced_numbers.sort()
        return sliced_numbers[1]