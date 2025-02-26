def find_second_largest_num(numbers):
    if len(numbers) < 81:
        return None
    end_index = min(201, len(numbers))
    sublist = numbers[80:end_index]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    second_largest = max((num for num in sublist if num != largest))
    return second_largest