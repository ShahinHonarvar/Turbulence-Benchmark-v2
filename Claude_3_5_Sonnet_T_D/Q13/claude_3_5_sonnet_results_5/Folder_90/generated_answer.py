def find_second_largest_num(numbers):
    if len(numbers) < 263:
        return None
    end_index = min(746, len(numbers) - 1)
    sublist = numbers[262:end_index + 1]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    second_largest = max((num for num in sublist if num != largest))
    return second_largest if second_largest != largest else None