def find_second_largest_num(numbers):
    if len(numbers) < 35:
        return None
    sublist = numbers[31:35]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    second_largest = max((num for num in sublist if num != largest))
    return second_largest if second_largest != largest else None