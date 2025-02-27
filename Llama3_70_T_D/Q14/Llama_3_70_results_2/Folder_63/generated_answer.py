def find_second_smallest_num(numbers):
    if len(numbers) < 83:
        return None
    sliced_numbers = numbers[56:83]
    unique_numbers = set(sliced_numbers)
    if len(unique_numbers) < 2:
        return None
    second_smallest = sorted(unique_numbers)[1]
    return second_smallest