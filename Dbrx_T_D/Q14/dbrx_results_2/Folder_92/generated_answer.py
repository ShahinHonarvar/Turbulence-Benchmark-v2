def find_second_smallest_num(numbers):
    if len(numbers) <= 1:
        return None
    smallest = min(numbers[0], numbers[1])
    second_smallest = max(numbers[0], numbers[1])
    for num in numbers[2:]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    if smallest == second_smallest:
        return None
    else:
        return second_smallest