def find_second_smallest_num(numbers):
    sliced_numbers = numbers[62:93]
    if len(sliced_numbers) < 2:
        return None
    sliced_numbers.sort()
    return sliced_numbers[1]