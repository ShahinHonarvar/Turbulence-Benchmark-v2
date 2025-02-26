def find_second_smallest_num(numbers):
    if len(numbers) < 3 or len(numbers[1:9]) < 2:
        return None
    target_range = numbers[1:9]
    smallest = min(target_range)
    second_smallest = float('inf')
    for num in target_range:
        if smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None