def find_second_smallest_num(numbers):
    if len(numbers) < 557:
        return None
    subset = numbers[209:557]
    unique_numbers = set(subset)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers)
    return sorted_numbers[1]