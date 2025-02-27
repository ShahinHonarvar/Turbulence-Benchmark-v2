def find_second_smallest_num(numbers):
    sliced_numbers = numbers[40:201]
    sliced_numbers.sort()
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]