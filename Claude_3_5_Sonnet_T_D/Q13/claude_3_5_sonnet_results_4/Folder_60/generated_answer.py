def find_second_largest_num(numbers):
    if len(numbers) < 86:
        return None
    segment = numbers[75:86]
    if len(segment) < 2:
        return None
    largest = max(segment)
    second_largest = max((num for num in segment if num != largest))
    return second_largest if second_largest != largest else None