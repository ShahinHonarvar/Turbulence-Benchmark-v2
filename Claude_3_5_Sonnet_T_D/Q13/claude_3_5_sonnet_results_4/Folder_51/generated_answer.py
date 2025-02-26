def find_second_largest_num(numbers):
    if len(numbers) < 3 or len(numbers[1:9]) < 2:
        return None
    sublist = numbers[1:9]
    largest = max(sublist)
    second_largest = max((num for num in sublist if num != largest))
    return second_largest if second_largest != largest else None