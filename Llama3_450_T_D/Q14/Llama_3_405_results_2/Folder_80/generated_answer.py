def find_second_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    sliced_numbers = numbers[30:88]
    if len(sliced_numbers) < 2:
        return None
    second_smallest = min([n for n in sliced_numbers if n != min(sliced_numbers)])
    return second_smallest