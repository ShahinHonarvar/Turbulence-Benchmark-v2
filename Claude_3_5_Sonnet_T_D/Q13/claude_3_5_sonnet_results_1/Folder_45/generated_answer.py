def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    end_index = min(200, len(numbers) - 1)
    sublist = numbers[30:end_index + 1]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    second_largest = max((num for num in sublist if num != largest))
    return second_largest