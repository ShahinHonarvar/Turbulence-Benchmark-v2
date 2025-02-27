def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 40 or len(numbers) < 28:
        return None
    smallest = min(numbers[28:40])
    second_smallest = None
    for num in numbers[28:40]:
        if num > smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    if second_smallest is None or second_smallest == smallest:
        return None
    return second_smallest