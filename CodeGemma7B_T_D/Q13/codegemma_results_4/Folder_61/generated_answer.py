def find_second_largest_num(numbers):
    if len(numbers) <= 1 or any((num in numbers[8:] for num in numbers[:8])):
        return None
    return sorted(numbers)[7]