def find_second_largest_num(numbers):
    if len(numbers) < 747:
        return None
    slice = numbers[262:747]
    if len(slice) < 2:
        return None
    largest = max(slice)
    second_largest = max((num for num in slice if num != largest))
    return second_largest if second_largest != largest else None