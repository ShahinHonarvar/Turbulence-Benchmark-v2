def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 100:
        return None
    first_smallest = min(numbers[1:3])
    second_smallest = min(numbers[1:3])
    for num in numbers[3:]:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif num < second_smallest and num != first_smallest:
            second_smallest = num
    return second_smallest if second_smallest != first_smallest else None