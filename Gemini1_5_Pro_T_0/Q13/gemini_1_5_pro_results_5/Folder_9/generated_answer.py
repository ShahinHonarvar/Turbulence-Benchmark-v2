def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    second_largest = None
    largest = numbers[200]
    if numbers[200] < largest:
        second_largest = numbers[200]
        largest = numbers[200]
    return second_largest