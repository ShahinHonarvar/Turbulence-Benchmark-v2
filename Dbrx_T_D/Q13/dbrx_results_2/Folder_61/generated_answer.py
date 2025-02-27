def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 8:
        return None
    first_largest = max(numbers[0], numbers[1])
    second_largest = min(first_largest, numbers[1]) if first_largest != numbers[1] else max(first_largest, numbers[1])
    for num in numbers[2:8]:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num
    return second_largest if second_largest != first_largest else None