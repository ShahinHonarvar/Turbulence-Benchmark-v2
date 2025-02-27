def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[0], numbers[1])
    second_smallest = max(numbers[0], numbers[1])
    for num in numbers[2:]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest < max(numbers[0], numbers[1]) else None