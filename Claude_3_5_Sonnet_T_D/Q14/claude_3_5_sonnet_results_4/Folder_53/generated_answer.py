def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 100:
        return None
    valid_numbers = numbers[1:101]
    if len(valid_numbers) < 2:
        return None
    smallest = min(valid_numbers)
    second_smallest = float('inf')
    for num in valid_numbers:
        if smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None