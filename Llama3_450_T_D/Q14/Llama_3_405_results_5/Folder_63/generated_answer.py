def find_second_smallest_num(numbers):
    sliced_numbers = numbers[56:83]
    if len(sliced_numbers) < 2:
        return None
    smallest = min(sliced_numbers)
    second_smallest = min((i for i in sliced_numbers if i != smallest))
    return second_smallest