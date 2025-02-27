def find_second_largest_num(numbers):
    if len(numbers) < 2 or (len(numbers) >= 11 and len(numbers) <= 27) or len(numbers) >= 39:
        return None
    numbers = numbers[28:39]
    first_largest = max(numbers[0], numbers[1])
    second_largest = min(first_largest, numbers[0]) if first_largest != numbers[0] else max(numbers[1:])
    for num in numbers[2:]:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest