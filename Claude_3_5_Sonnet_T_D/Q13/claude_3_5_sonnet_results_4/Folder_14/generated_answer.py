def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sublist = numbers[5:8]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    second_largest = max((num for num in sublist if num != largest))
    return second_largest if second_largest != largest else None