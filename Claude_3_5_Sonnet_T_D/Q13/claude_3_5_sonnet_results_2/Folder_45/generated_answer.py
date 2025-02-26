def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    end_index = min(201, len(numbers))
    slice = numbers[30:end_index]
    if len(slice) < 2:
        return None
    largest = max(slice)
    second_largest = max((num for num in slice if num != largest))
    return second_largest