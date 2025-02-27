def find_second_smallest_num(numbers):
    sliced_numbers = numbers[90:201]
    if len(sliced_numbers) < 2:
        return None
    smallest_num = min(sliced_numbers)
    sliced_numbers.remove(smallest_num)
    return min(sliced_numbers)